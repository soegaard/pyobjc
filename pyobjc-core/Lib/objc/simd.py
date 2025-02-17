"""
Python representation for SIMD types in (Objective)C

This module only defines the vector types that are
used in framework bindings.
"""

import objc
import operator

__all__ = (
    "vector_float2",
    "vector_float3",
    "vector_float4",
    "vector_double2",
    "vector_double3",
    "vector_double4",
    "vector_short2",
    "vector_ushort2",
    "vector_ushort3",
    "vector_ushort4",
    "vector_int2",
    "vector_uint2",
    "vector_uint3",
    "vector_uchar16",
)


def make_type(
    name, zero, cast_type, count, len2_type=None, len3_type=None, is_signed=True
):
    # XXX: Add:
    # - Range checks/limits (for integer types)

    assert count > 0
    if count in (3, 4):
        assert len2_type is not None
    if count == 4:
        assert len3_type is not None

    if count > 4:

        def __init__(self, *values):
            if len(values) == 0:
                self._values = [zero] * count

            elif len(values) == 1:
                v = values[0]
                v = cast_type(v)

                self._values = [v] * count
            elif len(values) != count:
                raise ValueError(values)

            else:
                self._values = [cast_type(v) for v in values]

    else:

        def __init__(self, *values):
            if len(values) == 0:
                self._values = [zero] * count
                return

            parts = []
            for p in values:
                if isinstance(p, self.__class__):
                    parts.extend(p._values)
                elif len2_type is not None and isinstance(p, len2_type):
                    parts.extend(p._values)
                elif len3_type is not None and isinstance(p, len3_type):
                    parts.extend(p._values)
                else:
                    parts.append(cast_type(p))

            if len(parts) == 1:
                self._values = parts * count

            elif len(parts) == count:
                self._values = parts

            else:
                raise ValueError(f"Expecting {count} values, got {len(parts)}")

    def as_tuple(self):
        return tuple(self._values)

    def __repr__(self):
        return f"{name}({', '.join(map(str, self._values))})"

    def __len__(self):
        return count

    def __getitem__(self, idx):
        return self._values[idx]

    def __setitem__(self, idx, value):
        if not isinstance(idx, int):
            raise TypeError(idx)
        self._values[idx] = cast_type(value)

    def _cast_self(self, other):
        if not isinstance(other, self.__class__):
            try:
                return self.__class__(cast_type(other))
            except (ValueError, TypeError):
                return NotImplemented

        return other

    def __add__(self, other):
        other = self._cast_self(other)
        if other is NotImplemented:
            return NotImplemented

        return self.__class__(*(x + y for x, y in zip(self, other)))

    def __radd__(self, other):
        other = self._cast_self(other)
        if other is NotImplemented:
            return NotImplemented

        return self.__class__(*(y + x for x, y in zip(self, other)))

    def __mul__(self, other):
        other = self._cast_self(other)
        if other is NotImplemented:
            return NotImplemented

        return self.__class__(*(x * y for x, y in zip(self, other)))

    def __rmul__(self, other):
        other = self._cast_self(other)
        if other is NotImplemented:
            return NotImplemented

        return self.__class__(*(y * x for x, y in zip(self, other)))

    def __matmul__(self, other: "vector_float2") -> "vector_float2":
        other = self._cast_self(other)
        if other is NotImplemented:
            return NotImplemented

        return sum(x * y for x, y in zip(self, other))

    def __abs__(self):
        return self.__class__(*(abs(x) for x in self._values))

    def __eq__(self, other):
        other = self._cast_self(other)
        if other is NotImplemented:
            return NotImplemented

        return self._values == other._values

    def __ne__(self, other):
        other = self._cast_self(other)
        if other is NotImplemented:
            return NotImplemented

        return self._values != other._values

    def __lt__(self, other):
        other = self._cast_self(other)
        if other is NotImplemented:
            return NotImplemented

        return self._values < other._values

    def __le__(self, other):
        other = self._cast_self(other)
        if other is NotImplemented:
            return NotImplemented

        return self._values <= other._values

    def __gt__(self, other):
        other = self._cast_self(other)
        if other is NotImplemented:
            return NotImplemented

        return self._values > other._values

    def __ge__(self, other):
        other = self._cast_self(other)
        if other is NotImplemented:
            return NotImplemented

        return self._values >= other._values

    def __neg__(self):
        return self.__class__(*(-n for n in self._values))

    def __pos__(self):
        return self.__class__(self)

    class_dict = {
        "__slots__": ("_values",),
        "__init__": __init__,
        "as_tuple": as_tuple,
        "_cast_self": _cast_self,
        "__repr__": __repr__,
        "__len__": __len__,
        "__getitem__": __getitem__,
        "__setitem__": __setitem__,
        "__add__": __add__,
        "__radd__": __radd__,
        "__mul__": __mul__,
        "__rmul__": __rmul__,
        "__matmul__": __matmul__,
        "__abs__": __abs__,
        "__eq__": __eq__,
        "__ne__": __ne__,
        "__lt__": __lt__,
        "__le__": __le__,
        "__gt__": __gt__,
        "__ge__": __ge__,
    }

    if is_signed:
        class_dict.update(
            {
                "__neg__": __neg__,
                "__pos__": __pos__,
            }
        )

    if 2 <= count <= 4:

        @property
        def x(self):
            return self._values[0]

        @x.setter
        def x(self, value):
            self._values[0] = cast_type(value)

        @property
        def y(self):
            return self._values[1]

        @y.setter
        def y(self, value):
            self._values[1] = cast_type(value)

        class_dict["x"] = x
        class_dict["y"] = y

    if count == 2:

        @property
        def xy(self):
            return self.__class__(*self._values)

        @xy.setter
        def xy(self, value):
            if not isinstance(value, self.__class__):
                raise TypeError(value)
            self._values[:] = value._values[:]

        class_dict["xy"] = xy

    elif count in (3, 4):

        @property
        def z(self):
            return self._values[2]

        @z.setter
        def z(self, value):
            self._values[2] = cast_type(value)

        class_dict["z"] = z

        @property
        def xy(self):
            return len2_type(*self._values[0:2])

        @xy.setter
        def xy(self, value):
            if not isinstance(value, len2_type):
                raise TypeError(value)
            self._values[0:2] = value._values[0:2]

        class_dict["xy"] = xy

        @property
        def yz(self):
            return len2_type(*self._values[1:3])

        @yz.setter
        def yz(self, value):
            if not isinstance(value, len2_type):
                raise TypeError(value)
            self._values[1:3] = value._values[:]

        class_dict["yz"] = yz

    if count == 3:

        @property
        def xyz(self):
            return self.__class__(*self._values[0:3])

        @xyz.setter
        def xyz(self, value):
            if not isinstance(value, self.__class__):
                raise TypeError(value)
            self._values[0:3] = value._values[:]

        class_dict["xyz"] = xyz

    if count == 4:

        @property
        def xyz(self):
            return len3_type(*self._values[0:3])

        @xyz.setter
        def xyz(self, value):
            if not isinstance(value, len3_type):
                raise TypeError(value)
            self._values[0:3] = value._values[:]

        class_dict["xyz"] = xyz

        @property
        def w(self):
            return self._values[3]

        @w.setter
        def w(self, value):
            self._values[3] = cast_type(value)

        class_dict["w"] = w

        @property
        def zw(self):
            return len2_type(*self._values[2:4])

        @zw.setter
        def zw(self, value):
            if not isinstance(value, len2_type):
                raise TypeError(value)
            self._values[2:4] = value._values[:]

        class_dict["zw"] = zw

        @property
        def yzw(self):
            return len3_type(*self._values[1:4])

        @yzw.setter
        def yzw(self, value):
            if not isinstance(value, len3_type):
                raise TypeError(value)
            self._values[1:4] = value._values[:]

        class_dict["yzw"] = yzw

        @property
        def xyzw(self):
            return self.__class__(*self._values)

        @xyzw.setter
        def xyzw(self, value):
            if not isinstance(value, self.__class__):
                raise TypeError(value)
            self._values[:] = value._values[:]

        class_dict["xyzw"] = xyzw

    return type(name, (object,), class_dict)


"""
    class vector_float2:
        __slots__ = ('_values',)


        @property
        def x(self) -> float:
            return self._values[0]

        @x.setter
        def x(self, value: float) -> None:
            self._values[0] = value

        @property
        def y(self) -> float:
            return self._values[1]

        @x.setter
        def y(self, value :float) -> None:
            self._values[1] = value

        @property
        def xy(self) -> "vector_float2":
            return vector_float2(self)

        @xy.setter
        def xy(self, value: "vector_float2") -> None:
            if not isinstance(value, vector_float2):
                raise TypeError(value)

            self._values[:] = value._values[:]
"""

vector_float2 = make_type("vector_float2", 0.0, float, 2)
vector_float3 = make_type("vector_float3", 0.0, float, 3, vector_float2)
vector_float4 = make_type("vector_float4", 0.0, float, 4, vector_float2, vector_float3)

vector_double2 = make_type("vector_double2", 0.0, float, 2)
vector_double3 = make_type("vector_double3", 0.0, float, 3, vector_double2)
vector_double4 = make_type(
    "vector_double4", 0.0, float, 4, vector_double2, vector_double3
)

vector_short2 = make_type("vector_short2", 0, operator.index, 2)
vector_ushort2 = make_type("vector_ushort2", 0, operator.index, 2, is_signed=False)
vector_ushort3 = make_type(
    "vector_ushort3", 0, operator.index, 3, vector_ushort2, is_signed=False
)
vector_ushort4 = make_type(
    "vector_ushort4",
    0,
    operator.index,
    4,
    vector_ushort2,
    vector_ushort3,
    is_signed=False,
)

vector_int2 = make_type("vector_int2", 0, operator.index, 2)
vector_uint2 = make_type("vector_uint2", 0, operator.index, 2, is_signed=False)
vector_uint3 = make_type(
    "vector_uint3", 0, operator.index, 3, vector_uint2, is_signed=False
)

vector_uchar16 = make_type("vector_uchar16", 0, operator.index, 16, is_signed=False)


if 0:
    # XXX: Add math operators
    matrix_float2x2 = objc.createStructType(
        "matrix_float2x2", b"{matrix_float2x2=[2<2f>]}", ["columns"]
    )
    matrix_float3x3 = objc.createStructType(
        "matrix_float3x3", b"{matrix_float3x3=[3<3f>]}", ["columns"]
    )
    matrix_float4x3 = objc.createStructType(
        "matrix_float4x3", b"{matrix_float4x3=[4<3f>]}", ["columns"]
    )
    matrix_float4x4 = objc.createStructType(
        "matrix_float4x4", b"{matrix_float4x4=[4<3f>]}", ["columns"]
    )
    matrix_double4x4 = objc.createStructType(
        "matrix_double4x4", b"{matrix_double4x4=[4<3f>]}", ["columns"]
    )
    simd_quadf = objc.createStructType("quadf", b"{simd_quadf=[<4f>]}", ["vector"])
    simd_quadd = objc.createStructType("quadf", b"{simd_quadd=[<4d>]}", ["vector"])
