#include <Python.h>
void print_python_bytes(PyObject *p);
void print_python_list(PyObject *p);
void print_python_float(PyObject *p);
/**
 * print_python_list - A function that print all the python list object
 * @p: Pointer to the all list
 * Return: Object list
 */
void print_python_list(PyObject *p)
{
	long valued;
	double value;
	const char *values;

	if (!PyList_Check(p))
	{
		fprintf(stderr, "[*] Python list info\n");
		fprintf(stderr, "  [ERROR] Invalid List Object\n");
		return;
	}

	Py_ssize_t size = PyList_Size(p);
	Py_ssize_t allocated = ((PyListObject *)p)->allocated;

	fprintf(stdout, "[*] Python list info\n");
	fprintf(stdout, "[*] Size of the Python List = %zd\n", size);
	fprintf(stdout, "[*] Allocated = %zd\n", allocated);

	for (Py_ssize_t i = 0; i < size; ++i)
	{
		PyObject *elem = PyList_GetItem(p, i);

		fprintf(stdout, "Element %zd: ", i);

		if (elem == NULL)
		{
			fprintf(stdout, "Type: <NULL>\n");
			continue;
		}
		else if (PyLong_Check(elem))
		{
			fprintf(stdout, "Type: Integer\n");
			valued = PyLong_AsLong(elem);
			fprintf(stdout, "Value: %ld\n", valued);
		}
		else if (PyFloat_Check(elem))
		{
			fprintf(stdout, "Type: Float\n");
			value = PyFloat_AsDouble(elem);
			fprintf(stdout, "Value: %f\n", value);
		}
		else if (PyUnicode_Check(elem))
		{
			fprintf(stdout, "Type: String\n");
			values = PyUnicode_AsUTF8(elem);
			fprintf(stdout, "Value: %s\n", values);
		}
		else
		{
			fprintf(stdout, "Type: Other\n");
		}
	}
}
/**
 * print_python_bytes - A function that print pythone byte
 * @p: Pointer to python list
 * Return: bytes in the python list
 */
void print_python_bytes(PyObject *p)
{
	if (!PyBytes_Check(p))
	{
		fprintf(stderr, "[.] bytes object info\n");
		fprintf(stderr, "  [ERROR] Invalid Bytes Object\n");
		return;
	}

	Py_ssize_t size = PyBytes_Size(p);

	fprintf(stdout, "[.] bytes object info\n");
	fprintf(stdout, "  size: %zd\n", size);

	Py_ssize_t max_print = size > 10 ? 10 : size;

	fprintf(stdout, "  first %zd bytes: ", max_print);
	for (Py_ssize_t i = 0; i < max_print; ++i)
	{
		fprintf(stdout, "%02x ", (unsigned char)PyBytes_AS_STRING(p)[i]);
	}
	fprintf(stdout, "\n");
}
/**
 * print_python_float - A function that print Python float
 * @p: Pointer to the pythone list
 * Return: Float list in the python object
 */
void print_python_float(PyObject *p)
{
	double value;

	if (!PyFloat_Check(p))
	{
		fprintf(stderr, "[.] float object info\n");
		fprintf(stderr, "  [ERROR] Invalid Float Object\n");
		return;
	}

	value = PyFloat_AS_DOUBLE(p);

	fprintf(stdout, "[.] float object info\n");
	fprintf(stdout, "  value: %f\n", value);
}
