#include <Python.h>
#include <stdio.h>

void print_python_list_info(PyObject *p)
{
	Py_ssize_t size;
	Py_ssize_t allocated;
	Py_ssize_t i;

	size = Py_SIZE(p);
	allocated = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocated);

	for (i = 0; i < size; i++)
	{
		printf("Element %ld: %s\n", i,
		       Py_TYPE(PyList_GetItem(p, i))->tp_name);
	}
}
