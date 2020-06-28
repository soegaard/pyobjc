#define Py_LIMITED_API 0x03060000
#define PY_SSIZE_T_CLEAN
#include "Python.h"
#include "pyobjc-api.h"

#import <AutomaticAssessmentConfiguration/AutomaticAssessmentConfiguration.h>
#import <Foundation/Foundation.h>

/* We include the source code here instead of
 * using the linker due to limitations in pyobjc-api.h
 */
#include "_AutomaticAssessmentConfiguration_protocols.m"

static PyMethodDef mod_methods[] = {
    {0, 0, 0, 0} /* sentinel */
};

/* Python glue */
PyObjC_MODULE_INIT(_AutomaticAssessmentConfiguration)
{
    PyObject* m;
    m = PyObjC_MODULE_CREATE(_AutomaticAssessmentConfiguration) if (!m) { PyObjC_INITERROR(); }

    PyObjC_INITDONE();
}
