/*
# AUTOGENERATED DO NOT EDIT

# If you edit this file, delete the AUTOGENERATED line to prevent re-generation
# BUILD api_versions [0x001]
*/

%module occlusion_query

#define __version__ "$Revision: 1.1.2.1 $"
#define __date__ "$Date: 2004/11/15 07:38:07 $"
#define __api_version__ API_VERSION
#define __author__ "PyOpenGL Developers <pyopengl-devel@lists.sourceforge.net>"
#define __doc__ ""

%{
/**
 *
 * GL.NV.occlusion_query Module for PyOpenGL
 * 
 * Authors: PyOpenGL Developers <pyopengl-devel@lists.sourceforge.net>
 * 
***/
%}

%include util.inc
%include gl_exception_handler.inc

%{
#ifdef CGL_PLATFORM
# include <OpenGL/glext.h>
#else
# include <GL/glext.h>
#endif

#if !EXT_DEFINES_PROTO || !defined(GL_NV_occlusion_query)
DECLARE_VOID_EXT(glGenOcclusionQueriesNV, (GLsizei n, GLuint *ids), (n, ids))
DECLARE_VOID_EXT(glDeleteOcclusionQueriesNV, (GLsizei n, const GLuint *ids), (n, ids))
DECLARE_EXT(glIsOcclusionQueryNV, GLboolean, 0, (GLuint id), (id))
DECLARE_VOID_EXT(glBeginOcclusionQueryNV, (GLuint id), (id))
DECLARE_VOID_EXT(glEndOcclusionQueryNV, (), ())
DECLARE_VOID_EXT(glGetOcclusionQueryivNV, (GLuint id, GLenum pname, GLint *params), (id, pname, params))
DECLARE_VOID_EXT(glGetOcclusionQueryuivNV, (GLuint id, GLenum pname, GLuint *params), (id, pname, params))
#endif
%}

/* FUNCTION DECLARATIONS */
void glGenOcclusionQueriesNV(GLsizei n, GLuint *ids);
DOC(glGenOcclusionQueriesNV, "glGenOcclusionQueriesNV(n, ids)")
void glDeleteOcclusionQueriesNV(GLsizei n, const GLuint *ids);
DOC(glDeleteOcclusionQueriesNV, "glDeleteOcclusionQueriesNV(n, ids)")
GLboolean glIsOcclusionQueryNV(GLuint id);
DOC(glIsOcclusionQueryNV, "glIsOcclusionQueryNV(id)")
void glBeginOcclusionQueryNV(GLuint id);
DOC(glBeginOcclusionQueryNV, "glBeginOcclusionQueryNV(id)")
void glEndOcclusionQueryNV();
DOC(glEndOcclusionQueryNV, "glEndOcclusionQueryNV()")
void glGetOcclusionQueryivNV(GLuint id, GLenum pname, GLint *params);
DOC(glGetOcclusionQueryivNV, "glGetOcclusionQueryivNV(id, pname, params)")
void glGetOcclusionQueryuivNV(GLuint id, GLenum pname, GLuint *params);
DOC(glGetOcclusionQueryuivNV, "glGetOcclusionQueryuivNV(id, pname, params)")

/* CONSTANT DECLARATIONS */
#define       GL_PIXEL_COUNTER_BITS_NV 0x8864
#define GL_CURRENT_OCCLUSION_QUERY_ID_NV 0x8865
#define              GL_PIXEL_COUNT_NV 0x8866
#define    GL_PIXEL_COUNT_AVAILABLE_NV 0x8867


%{
static char *proc_names[] =
{
#if !EXT_DEFINES_PROTO || !defined(GL_NV_occlusion_query)
"glGenOcclusionQueriesNV",
"glDeleteOcclusionQueriesNV",
"glIsOcclusionQueryNV",
"glBeginOcclusionQueryNV",
"glEndOcclusionQueryNV",
"glGetOcclusionQueryivNV",
"glGetOcclusionQueryuivNV",
#endif
	NULL
};

#define glInitOcclusionQueryNV() InitExtension("GL_NV_occlusion_query", proc_names)
%}

int glInitOcclusionQueryNV();
DOC(glInitOcclusionQueryNV, "glInitOcclusionQueryNV() -> bool")

%{
PyObject *__info()
{
	if (glInitOcclusionQueryNV())
	{
		PyObject *info = PyList_New(0);
		return info;
	}
	
	Py_INCREF(Py_None);
	return Py_None;
}
%}

PyObject *__info();

