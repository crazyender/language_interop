#include "Python.h"

void* py2voidptr(PyObject *o)
{
    void* a = o;
    return a;
}

PyObject* voidptr2py(void* a)
{
    PyObject *o = (PyObject *) a;
    Py_XINCREF(o);
    return o;
}

void** py2voidptrptr(PyObject *o)
{
    void* a = o;
    return &a;
}


