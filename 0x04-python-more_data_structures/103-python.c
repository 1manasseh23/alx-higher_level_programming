#include <Python.h>
#include <stdio.h>

/**
void print_python_list(PyObject *p)
{
	Py_ssize_t size, i;
	PyObject *element;

	printf("[*] Python list info\n");
	size = PyList_Size(p);
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		element = PyList_GetItem(p, i);
		printf("Element %ld: ", i);

		if (PyBytes_Check(element))
		{
			printf("bytes\n");
			print_python_list(element);
		}
		else if (PyList_Check(element))
		{
			printf("List\n");
			print_python_list(element);
		}
		else if (PyTuple_Check(element))
		{
			printf("tuple\n");
			print_python_list(element);
		}
		else if (PyFloat_Check(element))
		{
			printf("float\n");
		}
		else if (PyLong_Check(element))
		{
			printf("int\n");
		}
		else if (PyUnicode_Check(element))
		{
			printf("str\n");
		}
		else
		{
			printf("other\n");
		}
	}
}

void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	unsigned char *str;

	printf("[.] bytes object info\n");
	size = PyBytes_Size(p);
	printf(" size: %ld\n", size);

	str = (unsigned char *)PyBytes_AsString(p);
	printf(" trying string: %s\n", str);

	printf(" first %d bytes: ", size > 10 ? 10 : (int)size);
	for (i = 0; i < (size > 10 ? 10 : size); i++)
	{
		printf("%02x ", str[i]);
	}
	printf("\n");
}
*/

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

void print_python_list(PyObject *p) {
    Py_ssize_t size, i;
    PyObject *element;

    printf("[*] Python list info\n");
    size = PyList_Size(p);
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < size; i++) {
        element = PyList_GetItem(p, i);
        printf("Element %ld: ", i);

        if (PyBytes_Check(element)) {
            printf("bytes\n");
            print_python_bytes(element);
        } else if (PyList_Check(element)) {
            printf("List\n");
            print_python_list(element);
        } else if (PyTuple_Check(element)) {
            printf("tuple\n");
            print_python_list(element);
        } else if (PyFloat_Check(element)) {
            printf("float\n");
        } else if (PyLong_Check(element)) {
            printf("int\n");
        } else if (PyUnicode_Check(element)) {
            printf("str\n");
        } else {
            printf("other\n");
        }
    }
}

void print_python_bytes(PyObject *p) {
    Py_ssize_t size, i;
    unsigned char *str;

    printf("[.] bytes object info\n");
    size = PyBytes_Size(p);
    printf(" size: %ld\n", size);

    str = (unsigned char *)PyBytes_AsString(p);
    printf(" trying string: %s\n", str ? (char *)str : "[ERROR] Invalid Bytes Object");

    printf(" first %d bytes: ", size > 10 ? 10 : (int)size);
    for (i = 0; i < (size > 10 ? 10 : size); i++) {
        printf("%02x ", str[i]);
    }
    printf("\n");
}
