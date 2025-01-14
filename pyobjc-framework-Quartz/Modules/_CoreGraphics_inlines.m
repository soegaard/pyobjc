#define Py_LIMITED_API 0x03060000
#define PY_SSIZE_T_CLEAN
#include "Python.h"
#include "pyobjc-api.h"
#import <ApplicationServices/ApplicationServices.h>

/*
 * The definitions below can cause warnings when using
 * -Wunguarded-availability, but those warnings are harmless
 * because the functions are inline functions and hence will
 * be available on all macOS versions once compiled.
 */
#if PyObjC_BUILD_RELEASE >= 1013
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wunguarded-availability"
#endif

static PyObjC_function_map function_map[] = {
#if PyObjC_BUILD_RELEASE >= 1009
    {"CGVectorMake", (PyObjC_Function_Pointer)&CGVectorMake},
#endif
    {"CGPointMake", (PyObjC_Function_Pointer)&CGPointMake},
    {"CGRectMake", (PyObjC_Function_Pointer)&CGRectMake},
    {"CGSizeMake", (PyObjC_Function_Pointer)&CGSizeMake},
    {"__CGAffineTransformMake", (PyObjC_Function_Pointer)&__CGAffineTransformMake},
    {"__CGPointApplyAffineTransform",
     (PyObjC_Function_Pointer)&__CGPointApplyAffineTransform},
    {"__CGSizeApplyAffineTransform",
     (PyObjC_Function_Pointer)&__CGSizeApplyAffineTransform},
    {0, 0}};

#if PyObjC_BUILD_RELEASE >= 1013
#pragma clang diagnostic pop
#endif

static PyMethodDef mod_methods[] = {
    {0, 0, 0, 0} /* sentinel */
};

static struct PyModuleDef mod_module = {
    PyModuleDef_HEAD_INIT, "_inlines", NULL, 0, mod_methods, NULL, NULL, NULL, NULL};

PyObject* PyInit__inlines(void);

PyObject* __attribute__((__visibility__("default"))) PyInit__inlines(void)
{
    PyObject* m = PyModule_Create(&mod_module);
    if (!m)
        return NULL;

    if (PyModule_AddObject(m, "_inline_list_", PyObjC_CreateInlineTab(function_map)) < 0)
        return NULL;

    return m;
}
