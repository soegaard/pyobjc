# This file was created automatically by SWIG.
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _imaging

def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "this"):
        if isinstance(value, class_type):
            self.__dict__[name] = value.this
            if hasattr(value,"thisown"): self.__dict__["thisown"] = value.thisown
            del value.thisown
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static) or hasattr(self,name) or (name == "thisown"):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError,name

import types
try:
    _object = types.ObjectType
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0
del types


__version__ = _imaging.__version__
__date__ = _imaging.__date__
__api_version__ = _imaging.__api_version__
__author__ = _imaging.__author__
__doc__ = _imaging.__doc__
GL_CONSTANT_COLOR = _imaging.GL_CONSTANT_COLOR
GL_ONE_MINUS_CONSTANT_COLOR = _imaging.GL_ONE_MINUS_CONSTANT_COLOR
GL_CONSTANT_ALPHA = _imaging.GL_CONSTANT_ALPHA
GL_ONE_MINUS_CONSTANT_ALPHA = _imaging.GL_ONE_MINUS_CONSTANT_ALPHA
GL_BLEND_COLOR = _imaging.GL_BLEND_COLOR
GL_FUNC_ADD = _imaging.GL_FUNC_ADD
GL_MIN = _imaging.GL_MIN
GL_MAX = _imaging.GL_MAX
GL_BLEND_EQUATION = _imaging.GL_BLEND_EQUATION
GL_FUNC_SUBTRACT = _imaging.GL_FUNC_SUBTRACT
GL_FUNC_REVERSE_SUBTRACT = _imaging.GL_FUNC_REVERSE_SUBTRACT
GL_CONVOLUTION_1D = _imaging.GL_CONVOLUTION_1D
GL_CONVOLUTION_2D = _imaging.GL_CONVOLUTION_2D
GL_SEPARABLE_2D = _imaging.GL_SEPARABLE_2D
GL_CONVOLUTION_BORDER_MODE = _imaging.GL_CONVOLUTION_BORDER_MODE
GL_CONVOLUTION_FILTER_SCALE = _imaging.GL_CONVOLUTION_FILTER_SCALE
GL_CONVOLUTION_FILTER_BIAS = _imaging.GL_CONVOLUTION_FILTER_BIAS
GL_REDUCE = _imaging.GL_REDUCE
GL_CONVOLUTION_FORMAT = _imaging.GL_CONVOLUTION_FORMAT
GL_CONVOLUTION_WIDTH = _imaging.GL_CONVOLUTION_WIDTH
GL_CONVOLUTION_HEIGHT = _imaging.GL_CONVOLUTION_HEIGHT
GL_MAX_CONVOLUTION_WIDTH = _imaging.GL_MAX_CONVOLUTION_WIDTH
GL_MAX_CONVOLUTION_HEIGHT = _imaging.GL_MAX_CONVOLUTION_HEIGHT
GL_POST_CONVOLUTION_RED_SCALE = _imaging.GL_POST_CONVOLUTION_RED_SCALE
GL_POST_CONVOLUTION_GREEN_SCALE = _imaging.GL_POST_CONVOLUTION_GREEN_SCALE
GL_POST_CONVOLUTION_BLUE_SCALE = _imaging.GL_POST_CONVOLUTION_BLUE_SCALE
GL_POST_CONVOLUTION_ALPHA_SCALE = _imaging.GL_POST_CONVOLUTION_ALPHA_SCALE
GL_POST_CONVOLUTION_RED_BIAS = _imaging.GL_POST_CONVOLUTION_RED_BIAS
GL_POST_CONVOLUTION_GREEN_BIAS = _imaging.GL_POST_CONVOLUTION_GREEN_BIAS
GL_POST_CONVOLUTION_BLUE_BIAS = _imaging.GL_POST_CONVOLUTION_BLUE_BIAS
GL_POST_CONVOLUTION_ALPHA_BIAS = _imaging.GL_POST_CONVOLUTION_ALPHA_BIAS
GL_HISTOGRAM = _imaging.GL_HISTOGRAM
GL_PROXY_HISTOGRAM = _imaging.GL_PROXY_HISTOGRAM
GL_HISTOGRAM_WIDTH = _imaging.GL_HISTOGRAM_WIDTH
GL_HISTOGRAM_FORMAT = _imaging.GL_HISTOGRAM_FORMAT
GL_HISTOGRAM_RED_SIZE = _imaging.GL_HISTOGRAM_RED_SIZE
GL_HISTOGRAM_GREEN_SIZE = _imaging.GL_HISTOGRAM_GREEN_SIZE
GL_HISTOGRAM_BLUE_SIZE = _imaging.GL_HISTOGRAM_BLUE_SIZE
GL_HISTOGRAM_ALPHA_SIZE = _imaging.GL_HISTOGRAM_ALPHA_SIZE
GL_HISTOGRAM_LUMINANCE_SIZE = _imaging.GL_HISTOGRAM_LUMINANCE_SIZE
GL_HISTOGRAM_SINK = _imaging.GL_HISTOGRAM_SINK
GL_MINMAX = _imaging.GL_MINMAX
GL_MINMAX_FORMAT = _imaging.GL_MINMAX_FORMAT
GL_MINMAX_SINK = _imaging.GL_MINMAX_SINK
GL_TABLE_TOO_LARGE = _imaging.GL_TABLE_TOO_LARGE
GL_COLOR_MATRIX = _imaging.GL_COLOR_MATRIX
GL_COLOR_MATRIX_STACK_DEPTH = _imaging.GL_COLOR_MATRIX_STACK_DEPTH
GL_MAX_COLOR_MATRIX_STACK_DEPTH = _imaging.GL_MAX_COLOR_MATRIX_STACK_DEPTH
GL_POST_COLOR_MATRIX_RED_SCALE = _imaging.GL_POST_COLOR_MATRIX_RED_SCALE
GL_POST_COLOR_MATRIX_GREEN_SCALE = _imaging.GL_POST_COLOR_MATRIX_GREEN_SCALE
GL_POST_COLOR_MATRIX_BLUE_SCALE = _imaging.GL_POST_COLOR_MATRIX_BLUE_SCALE
GL_POST_COLOR_MATRIX_ALPHA_SCALE = _imaging.GL_POST_COLOR_MATRIX_ALPHA_SCALE
GL_POST_COLOR_MATRIX_RED_BIAS = _imaging.GL_POST_COLOR_MATRIX_RED_BIAS
GL_POST_COLOR_MATRIX_GREEN_BIAS = _imaging.GL_POST_COLOR_MATRIX_GREEN_BIAS
GL_POST_COLOR_MATRIX_BLUE_BIAS = _imaging.GL_POST_COLOR_MATRIX_BLUE_BIAS
GL_POST_COLOR_MATRIX_ALPHA_BIAS = _imaging.GL_POST_COLOR_MATRIX_ALPHA_BIAS
GL_COLOR_TABLE = _imaging.GL_COLOR_TABLE
GL_POST_CONVOLUTION_COLOR_TABLE = _imaging.GL_POST_CONVOLUTION_COLOR_TABLE
GL_POST_COLOR_MATRIX_COLOR_TABLE = _imaging.GL_POST_COLOR_MATRIX_COLOR_TABLE
GL_PROXY_COLOR_TABLE = _imaging.GL_PROXY_COLOR_TABLE
GL_PROXY_POST_CONVOLUTION_COLOR_TABLE = _imaging.GL_PROXY_POST_CONVOLUTION_COLOR_TABLE
GL_PROXY_POST_COLOR_MATRIX_COLOR_TABLE = _imaging.GL_PROXY_POST_COLOR_MATRIX_COLOR_TABLE
GL_COLOR_TABLE_SCALE = _imaging.GL_COLOR_TABLE_SCALE
GL_COLOR_TABLE_BIAS = _imaging.GL_COLOR_TABLE_BIAS
GL_COLOR_TABLE_FORMAT = _imaging.GL_COLOR_TABLE_FORMAT
GL_COLOR_TABLE_WIDTH = _imaging.GL_COLOR_TABLE_WIDTH
GL_COLOR_TABLE_RED_SIZE = _imaging.GL_COLOR_TABLE_RED_SIZE
GL_COLOR_TABLE_GREEN_SIZE = _imaging.GL_COLOR_TABLE_GREEN_SIZE
GL_COLOR_TABLE_BLUE_SIZE = _imaging.GL_COLOR_TABLE_BLUE_SIZE
GL_COLOR_TABLE_ALPHA_SIZE = _imaging.GL_COLOR_TABLE_ALPHA_SIZE
GL_COLOR_TABLE_LUMINANCE_SIZE = _imaging.GL_COLOR_TABLE_LUMINANCE_SIZE
GL_COLOR_TABLE_INTENSITY_SIZE = _imaging.GL_COLOR_TABLE_INTENSITY_SIZE
GL_CONSTANT_BORDER = _imaging.GL_CONSTANT_BORDER
GL_REPLICATE_BORDER = _imaging.GL_REPLICATE_BORDER
GL_CONVOLUTION_BORDER_COLOR = _imaging.GL_CONVOLUTION_BORDER_COLOR

glInitImagingARB = _imaging.glInitImagingARB

__info = _imaging.__info

