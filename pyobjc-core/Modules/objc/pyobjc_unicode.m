/*
 * Custom subclass of PyUnicode_Type, to allow for transparent bridging of
 * strings
 *
 * XXX: The code in this file has too much knowledge about the
 *      impl. of CPytho's Unicode type. Try to find a better solution
 *      (which might require changes to CPython...)
 *
 * XXX: This type is needed because it is not possible to have a
 *      type that behaves like a string, but isn't a subclass of
 *      PyUnicode_Type. At least not when the CPython C API is involved :-(.
 */

#include "pyobjc.h"

#include <Foundation/NSString.h>
#include <stddef.h>

NS_ASSUME_NONNULL_BEGIN

typedef struct {
    PyUnicodeObject base;
    PyObject* _Nullable weakrefs;
    id nsstr;
    PyObject* _Nullable py_nsstr;

} PyObjCUnicodeObject;

PyDoc_STRVAR(class_doc, "objc.pyobjc_unicode\n"
                        "\n"
                        "Subclass of unicode for representing NSString values. Use\n"
                        "the method nsstring to access the NSString.\n"
                        "\n"
                        "Note that instances are immutable and won't be updated when\n"
                        "the value of the NSString changes.");

static void
class_dealloc(PyObject* obj)
{
    PyObjCUnicodeObject* uobj     = (PyObjCUnicodeObject*)obj;
    PyObject*            weakrefs = uobj->weakrefs;
    PyObject*            py_nsstr = uobj->py_nsstr;

    PyObjC_UnregisterPythonProxy(uobj->nsstr, obj);
    Py_CLEAR(py_nsstr);

    if (weakrefs) {
        PyObject_ClearWeakRefs(obj);
    }

    [uobj->nsstr release];

    PyUnicode_Type.tp_dealloc(obj);
}

static PyObject* _Nullable meth_nsstring(PyObject* self)
{
    PyObjCUnicodeObject* uobj = (PyObjCUnicodeObject*)self;

    if (uobj->py_nsstr == NULL) {
        uobj->py_nsstr = PyObjCObject_New(
            uobj->nsstr, PyObjCObject_kDEFAULT | PyObjCObject_kNEW_WRAPPER, YES);
        if (uobj->py_nsstr == NULL) { // LCOV_BR_EXCL_LINE
            return NULL;              // LCOV_EXCL_LINE
        }
    }
    Py_INCREF(uobj->py_nsstr);
    return uobj->py_nsstr;
}

static PyObject* _Nullable meth_getattro(PyObject* o, PyObject* attr_name)
{
    PyObject* res;
    res = PyObject_GenericGetAttr(o, attr_name);
    if (res == NULL) {
        PyObject* py_nsstr;

        PyErr_Clear();
        py_nsstr = meth_nsstring(o);
        if (py_nsstr == NULL) { // LCOV_BR_EXCL_LINE
            return NULL;        // LCOV_EXCL_LINE
        }
        res = PyObject_GetAttr(py_nsstr, attr_name);
        Py_DECREF(py_nsstr);
    }
    return res;
}

static PyObject* _Nullable meth_reduce(PyObject* self)
{
    PyObject* retVal = NULL;
    PyObject* v      = NULL;
    PyObject* v2     = NULL;

    retVal = PyTuple_New(2);
    if (retVal == NULL) // LCOV_BR_EXCL_LINE
        goto error;     // LCOV_EXCL_LINE

    v = (PyObject*)&PyUnicode_Type;
    Py_INCREF(v);
    PyTuple_SET_ITEM(retVal, 0, v);

    v = PyUnicode_FromObject(self);
    if (v == NULL)  // LCOV_BR_EXCL_LINE
        goto error; // LCOV_EXCL_LINE

    v2 = PyTuple_New(1);
    if (v2 == NULL) // LCOV_BR_EXCL_LINE
        goto error; // LCOV_EXCL_LINE
    PyTuple_SET_ITEM(v2, 0, v);
    PyTuple_SET_ITEM(retVal, 1, v2);

    return retVal;

error:
    // LCOV_EXCL_START
    Py_XDECREF(retVal);
    Py_XDECREF(v);
    return NULL;
    // LCOV_EXCL_STOP
}

static PyMethodDef class_methods[] = {{.ml_name  = "nsstring",
                                       .ml_meth  = (PyCFunction)meth_nsstring,
                                       .ml_flags = METH_NOARGS,
                                       .ml_doc   = "directly access NSString instance"},
                                      {
                                          .ml_name  = "__reduce__",
                                          .ml_meth  = (PyCFunction)meth_reduce,
                                          .ml_flags = METH_NOARGS,
                                      },
                                      {
                                          .ml_name = NULL /* SENTINEL */
                                      }};

static PyObject* _Nullable nsstring_get__pyobjc_object__(PyObject* self,
                                                         void* _Nullable closure
                                                         __attribute__((__unused__)))
{
    return meth_nsstring(self);
}

static PyGetSetDef nsstring_getsetters[] = {
    {
        .name = "__pyobjc_object__",
        .get  = (getter)nsstring_get__pyobjc_object__,
        .doc  = "raw NSString instance",
    },
    {
        .name = NULL /* SENTINEL */
    }};

static PyObject* _Nullable class_new(PyTypeObject* type __attribute__((__unused__)),
                                     PyObject*     args __attribute__((__unused__)),
                                     PyObject*     kwds __attribute__((__unused__)))
{
    PyErr_SetString(PyExc_TypeError,
                    "Cannot create instances of 'objc.unicode' in Python");
    return NULL;
}

PyTypeObject PyObjCUnicode_Type = {
    PyVarObject_HEAD_INIT(&PyType_Type, 0).tp_name = "objc.pyobjc_unicode",
    .tp_basicsize                                  = sizeof(PyObjCUnicodeObject),
    .tp_itemsize                                   = 0,
    .tp_dealloc                                    = class_dealloc,
    .tp_getattro                                   = meth_getattro,
    .tp_flags                                      = Py_TPFLAGS_DEFAULT,
    .tp_doc                                        = class_doc,
    .tp_weaklistoffset = offsetof(PyObjCUnicodeObject, weakrefs),
    .tp_methods        = class_methods,
    .tp_getset         = nsstring_getsetters,
    .tp_base           = &PyUnicode_Type,
    .tp_new            = class_new,
};

/*
 * Python 3.3 introduced a new, more efficient representation
 * for unicode objects.
 *
 * This function cannot use the most efficient
 * representation where the character data is stored in the same
 * memory block as the object header because PyObjCUnicode adds
 * more data to the object header, which PyUnicode does not
 * expect.
 *
 * This function therefore creates a "legacy string, ready" (see
 * unicodeobject.h in the python 3.3 source tree for more information)
 *
 * NOTE: This function has deep knowledge about the layout of Unicode
 * objects in Python 3.3, and needs to be updated when that
 * layout changes in later versions of Python.
 */
PyObject* _Nullable PyObjCUnicode_New(NSString* value)
{
    PyObjCUnicodeObject*    result;
    PyASCIIObject*          ascii;
    PyCompactUnicodeObject* compact;

    NSInteger i, length;
    unichar*  characters = NULL;
    NSRange   range;
    Py_UCS4   maxchar;
    int       nr_surrogates;

    length = [value length];

    characters = PyObject_Malloc(sizeof(unichar) * (length + 1));
    if (characters == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        PyErr_NoMemory();
        return NULL;
        // LCOV_EXCL_STOP
    }

    bool have_exception = false;
    Py_BEGIN_ALLOW_THREADS
        @try {
            range = NSMakeRange(0, length);

            [value getCharacters:characters range:range];
            characters[length] = 0;

        } @catch (NSObject* localException) {
            have_exception = true;
            PyObjCErr_FromObjC(localException);
        }
    Py_END_ALLOW_THREADS

    if (have_exception) {
        PyObject_Free(characters);
        characters = NULL;

        return NULL;
    }

    result = PyObject_New(PyObjCUnicodeObject, &PyObjCUnicode_Type);
    if (result == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        PyObject_Free(characters);
        characters = NULL;

        return NULL;
        // LCOV_EXCL_STOP
    }

    result->weakrefs = NULL;
    result->py_nsstr = NULL;
    result->nsstr    = nil;

    ascii   = (PyASCIIObject*)result;
    compact = (PyCompactUnicodeObject*)result;

    ascii->hash   = -1;
    ascii->wstr   = NULL;
    ascii->length = length;

    ascii->state.compact  = 0;
    ascii->state.ready    = 1;
    ascii->state.interned = SSTATE_NOT_INTERNED;

    compact->utf8_length = 0;
    compact->utf8        = NULL;
    compact->wstr_length = 0;

    result->base.data.any = NULL;

    maxchar       = 0;
    nr_surrogates = 0;
    for (i = 0; i < length; i++) {
        Py_UCS4 cur = (Py_UCS4)characters[i];

        if (Py_UNICODE_IS_HIGH_SURROGATE(cur) && (i < length - 1)
            && (Py_UNICODE_IS_LOW_SURROGATE(characters[i + 1]))) {

            Py_UCS4 ch = Py_UNICODE_JOIN_SURROGATES(characters[i], characters[i + 1]);
            i++;
            nr_surrogates++;

            if (ch > maxchar) {
                maxchar = ch;
            }

        } else if (cur > maxchar) {
            maxchar = cur;
        }
    }

    if (maxchar <= 128) {
        ascii->state.ascii = 1;
        ascii->state.kind  = PyUnicode_1BYTE_KIND;

    } else if (maxchar <= 255) {
        ascii->state.ascii = 0;
        ascii->state.kind  = PyUnicode_1BYTE_KIND;

    } else if (maxchar <= 0xFFFF) {
        ascii->state.ascii = 0;
        ascii->state.kind  = PyUnicode_2BYTE_KIND;

    } else {
        ascii->state.ascii = 0;
        ascii->state.kind  = PyUnicode_4BYTE_KIND;
    }

    /* Create storage for the code points and copy the data */
    result->base.data.any = NULL;
    if (ascii->state.kind == PyUnicode_1BYTE_KIND) {
        Py_UCS1* latin1_cur;

        result->base.data.latin1 =
            PyObject_MALLOC(sizeof(Py_UCS1) * (length + 1 - nr_surrogates));
        if (result->base.data.latin1 == NULL) // LCOV_BR_EXCL_LINE
            goto error;                       // LCOV_EXCL_LINE

        latin1_cur = result->base.data.latin1;
        for (i = 0; i < length; i++) {
            if ( // LCOV_BR_EXCL_LINE
                Py_UNICODE_IS_HIGH_SURROGATE(characters[i]) && (i < length - 1)
                && (Py_UNICODE_IS_LOW_SURROGATE(characters[i + 1]))) {
                Py_UCS4 ch = Py_UNICODE_JOIN_SURROGATES(characters[i], characters[i + 1]);
                /* AFAIK  this cannot happen, surrogtes are outside of the range
                 * of 1BYTE_KIND, likewise for the decoded character.
                 */
                // LCOV_EXCL_START
                *latin1_cur++ = (Py_UCS1)ch;
                i++;
                // LCOV_EXCL_STOP

            } else {
                *latin1_cur++ = (Py_UCS1)characters[i];
            }
        }

        *latin1_cur   = 0;
        ascii->length = length - nr_surrogates;
        if (ascii->state.ascii) {
            /* With ASCII representation the UTF8 representation is
             * also known without further calculation, and MUST be
             * filled according to the spec
             */
            compact->utf8_length = length - nr_surrogates;
            compact->utf8        = (char*)result->base.data.latin1;
        }

    } else if (ascii->state.kind == PyUnicode_2BYTE_KIND) {
        if (nr_surrogates == 0) {
            /* No surrogates and 2BYTE_KIND, this means the unichar buffer
             * can be reused as storage for the python unicode string
             */
            ascii->length          = length;
            result->base.data.ucs2 = (Py_UCS2*)characters;
            characters             = NULL;

        } else {
            /* See above, this cannot happen because decoded surrogate
             * pairs are out of range.
             */
            // LCOV_EXCL_START
            Py_UCS2* ucs2_cur;

            result->base.data.ucs2 =
                PyObject_MALLOC(sizeof(Py_UCS2) * (length + 1 - nr_surrogates));
            if (result->base.data.ucs2 == NULL) // LCOV_BR_EXCL_LINE
                goto error;                     // LCOV_EXCL_LINE

            ucs2_cur = result->base.data.ucs2;
            for (i = 0; i < length; i++) {
                if (Py_UNICODE_IS_HIGH_SURROGATE(characters[i]) && (i < length - 1)
                    && (Py_UNICODE_IS_LOW_SURROGATE(characters[i + 1]))) {
                    Py_UCS4 ch =
                        Py_UNICODE_JOIN_SURROGATES(characters[i], characters[i + 1]);
                    *ucs2_cur++ = (Py_UCS2)ch;
                    i++;
                } else {
                    *ucs2_cur++ = (Py_UCS2)characters[i];
                }
            }
            ascii->length = length - nr_surrogates;
            *ucs2_cur     = 0;
            // LCOV_EXCL_STOP
        }

    } else { /* 4BYTE_KIND */
        Py_UCS4* ucs4_cur;

        result->base.data.ucs4 =
            PyObject_MALLOC(sizeof(Py_UCS4) * (length + 1 - nr_surrogates));
        if (result->base.data.ucs4 == NULL) { // LCOV_BR_EXCL_LINE
            goto error;                       // LCOV_EXCL_LINE
        }

        ucs4_cur = result->base.data.ucs4;
        for (i = 0; i < length; i++) {
            if (Py_UNICODE_IS_HIGH_SURROGATE(characters[i]) && (i < length - 1)
                && (Py_UNICODE_IS_LOW_SURROGATE(characters[i + 1]))) {
                Py_UCS4 ch = Py_UNICODE_JOIN_SURROGATES(characters[i], characters[i + 1]);

                if (ch > 0x10ffff) { // LCOV_BR_EXCL_LINE
                    // LCOV_EXCL_START
                    /* XXX: Cannot happen */
                    /* Unicode spec has a maximum code point value and
                     * Python 3.3 enforces this, keep surrogate pair
                     * to avoid an error.
                     */
                    *ucs4_cur++ = (Py_UCS4)characters[i];
                    // LCOV_EXCL_STOP
                } else { // LCOV_BR_EXCL_LINE
                    *ucs4_cur++ = (Py_UCS4)ch;
                    i++;
                }
            } else {
                *ucs4_cur++ = (Py_UCS4)characters[i];
            }
        }
        *ucs4_cur     = 0;
        ascii->length = length - nr_surrogates;

#if SIZEOF_WCHAR_T != 4
#error "Code assumes sizeof(wchar_t) == 4
#endif
        ascii->wstr          = (wchar_t*)result->base.data.ucs4;
        compact->wstr_length = ascii->length;
    }

    if (characters != NULL) {
        PyObject_Free(characters);
        characters = NULL;
    }

#ifdef Py_DEBUG
    /* Check that the unicode object is correct */
    _PyUnicode_CheckConsistency((PyObject*)result, 1);
#endif

    /* Finally store PyUnicode specific data */
    result->nsstr = [value retain];

    return (PyObject*)result;

error:
    // LCOV_EXCL_START
    Py_DECREF((PyObject*)result);
    PyObject_Free(characters);
    characters = NULL;
    PyErr_NoMemory();
    return NULL;
    // LCOV_EXCL_STOP
}

NS_ASSUME_NONNULL_END
