#include <Python.h>
#include "listobject.h"
#include "object.h"
void print_python_list_info(PyObject *p)
{
    Py_ssize_t size, i;
    PyListObject *list = (PyListObject *)p;

    size = PyList_Size(p);
    printf("[*] Size of the Python List = %zd\n", size);
    printf("[*] Allocated = %zd\n", list->allocated);

    for (i = 0; i < size; i++)
    {
	PyObject *element = list->ob_item[i];
        printf("Element %zd: %s\n", i, Py_TYPE(element)->tp_name);
    }
}
