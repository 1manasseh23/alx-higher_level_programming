#include <Python.h>
void print_python_bytes(PyObject *p);
void print_python_list(PyObject *p);
void print_python_float(PyObject *p);

void print_python_list(PyObject *p) {
    if (!PyList_Check(p)) {
        fprintf(stderr, "[*] Python list info\n");
        fprintf(stderr, "  [ERROR] Invalid List Object\n");
        return;
    }

    Py_ssize_t size = PyList_Size(p);
    Py_ssize_t allocated = ((PyListObject *)p)->allocated;

    fprintf(stdout, "[*] Python list info\n");
    fprintf(stdout, "[*] Size of the Python List = %zd\n", size);
    fprintf(stdout, "[*] Allocated = %zd\n", allocated);

    for (Py_ssize_t i = 0; i < size; ++i) {
        PyObject *elem = PyList_GetItem(p, i);
        // Extract info about each element in the list
        fprintf(stdout, "Element %zd: ", i);

        // Check the type of the element
        if (elem == NULL) {
            fprintf(stdout, "Type: <NULL>\n");
            continue;
        } else if (PyLong_Check(elem)) {
            fprintf(stdout, "Type: Integer\n");
            // Extract and print integer value
            long value = PyLong_AsLong(elem);
            fprintf(stdout, "Value: %ld\n", value);
        } else if (PyFloat_Check(elem)) {
            fprintf(stdout, "Type: Float\n");
            // Extract and print float value
            double value = PyFloat_AsDouble(elem);
            fprintf(stdout, "Value: %f\n", value);
        } else if (PyUnicode_Check(elem)) {
            fprintf(stdout, "Type: String\n");
            // Extract and print string value
            const char *value = PyUnicode_AsUTF8(elem);
            fprintf(stdout, "Value: %s\n", value);
        } else {
            fprintf(stdout, "Type: Other\n");
            // Handle other types as needed
            // You can add more checks for other types as necessary
        }
    }
}

void print_python_bytes(PyObject *p) {
	if (!PyBytes_Check(p)) {
		fprintf(stderr, "[.] bytes object info\n");
		fprintf(stderr, "  [ERROR] Invalid Bytes Object\n");
		return;
	}

	Py_ssize_t size = PyBytes_Size(p);
	fprintf(stdout, "[.] bytes object info\n");
	fprintf(stdout, "  size: %zd\n", size);

	// Print a maximum of 10 bytes
	Py_ssize_t max_print = size > 10 ? 10 : size;
	fprintf(stdout, "  first %zd bytes: ", max_print);
	for (Py_ssize_t i = 0; i < max_print; ++i) {
		fprintf(stdout, "%02x ", (unsigned char)PyBytes_AS_STRING(p)[i]);
	}
	fprintf(stdout, "\n");
}

void print_python_float(PyObject *p) {
	if (!PyFloat_Check(p)) {
		fprintf(stderr, "[.] float object info\n");
		fprintf(stderr, "  [ERROR] Invalid Float Object\n");
		return;
	}

	double value = PyFloat_AS_DOUBLE(p);
	fprintf(stdout, "[.] float object info\n");
	fprintf(stdout, "  value: %f\n", value);
}
