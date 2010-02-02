#include <Python.h>
#include "pyobjc-api.h"

#import <CoreFoundation/CoreFoundation.h>

static void* 
mod_retain(void* info) 
{
	PyGILState_STATE state = PyGILState_Ensure();
	Py_INCREF((PyObject*)info);
	PyGILState_Release(state);
	return info;
}

static void
mod_release(void* info)
{
	PyGILState_STATE state = PyGILState_Ensure();
	Py_DECREF((PyObject*)info);
	PyGILState_Release(state);
}


static CFStreamClientContext mod_CFStreamClientContext = {
	0,		
	NULL,
	mod_retain,
	mod_release,
	NULL
};

static void
mod_CFReadStreamClientCallBack(	
	CFReadStreamRef f,
	CFStreamEventType eventType,
	void* _info)
{
	PyObject* info = (PyObject*)_info;
	PyGILState_STATE state = PyGILState_Ensure();

	PyObject* py_f = PyObjC_ObjCToPython(@encode(CFReadStreamRef), &f);
	PyObject* py_eventType = PyObjC_ObjCToPython(
		@encode(CFStreamEventType), &eventType);

	PyObject* result = PyObject_CallFunction(
		PyTuple_GET_ITEM(info, 0),
		"NNO", py_f, py_eventType, PyTuple_GET_ITEM(info, 1));
	if (result == NULL) {
		PyObjCErr_ToObjCWithGILState(&state);
	}
	Py_DECREF(result);
	PyGILState_Release(state);
}

static PyObject*
mod_CFReadStreamSetClient(
	PyObject* self __attribute__((__unused__)),
	PyObject* args)
{
	PyObject* py_stream;
	PyObject* py_streamEvents;
	PyObject* callout;
	PyObject* info;
	CFReadStreamRef stream;
	CFOptionFlags streamEvents;
	CFStreamClientContext context;

	if (!PyArg_ParseTuple(args, "OOOO", &py_stream, &py_streamEvents, &callout, &info)) {
		return NULL;
	}

	if (PyObjC_PythonToObjC(@encode(CFReadStreamRef), py_stream, &stream) < 0) {
		return NULL;
	}
	if (PyObjC_PythonToObjC(@encode(CFOptionFlags), py_streamEvents, &streamEvents) < 0) {
		return NULL;
	}

	if (info != PyObjC_NULL) {
		context = mod_CFStreamClientContext;
		context.info = Py_BuildValue("OO", callout, info);
		if (context.info == NULL) {
			return NULL;
		}
	}


	Boolean rv = FALSE;
	PyObjC_DURING
		if (info == PyObjC_NULL) {
			rv = CFReadStreamSetClient(
				stream, streamEvents, 
				mod_CFReadStreamClientCallBack, NULL);
		} else {
			rv = CFReadStreamSetClient(
				stream, streamEvents, 
				mod_CFReadStreamClientCallBack, &context);
		}

		
	PyObjC_HANDLER
		rv = FALSE;
		PyObjCErr_FromObjC(localException);

	PyObjC_ENDHANDLER
	if (info != PyObjC_NULL) {
		Py_DECREF((PyObject*)context.info);
	}

	if (PyErr_Occurred()) {
		return NULL;
	}

	return PyBool_FromLong(rv);
}

static PyMethodDef mod_methods[] = {
        {
		"CFReadStreamSetClient",
		(PyCFunction)mod_CFReadStreamSetClient,
		METH_VARARGS,
		NULL
	},
	{ 0, 0, 0, 0 } /* sentinel */
};


/* Python glue */
#if PY_VERSION_HEX >= 0x03000000

static struct PyModuleDef mod_module = {
        PyModuleDef_HEAD_INIT,
	"_CFReadStream",
	NULL,
	0,
	mod_methods,
	NULL,
	NULL,
	NULL,
	NULL
};

#define INITERROR() return NULL
#define INITDONE() return m

PyObject* PyInit__CFReadStream(void);

PyObject*
PyInit__CFReadStream(void)

#else

#define INITERROR() return
#define INITDONE() return

void init_CFReadStream(void);

void
init_CFReadStream(void)
#endif
{
	PyObject* m;
#if PY_VERSION_HEX >= 0x03000000
	m = PyModule_Create(&mod_module);
#else
	m = Py_InitModule4("_CFReadStream", mod_methods,
		NULL, NULL, PYTHON_API_VERSION);
#endif
	if (!m) {
		INITERROR();
	}
	if (PyObjC_ImportAPI(m) == -1) INITERROR();

	INITDONE();
}
