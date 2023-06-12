#include <Python.h>
/**
 * print_python_list_info - c function to pirnt basic info about Python lists.
 * @p: A PyObject list.
 */
void print_python_list_info(PyObject *p)
{
	PyObject *pyObj;
	int size, MemAlloc, i = 0;

	MemAlloc = ((PyListObject *)p)->allocated;
	size = Py_SIZE(p);
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", MemAlloc);
	for (; i < size;)
	{
		printf("Element %d: ", i);
		pyObj = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(pyObj)->tp_name);
		i++;
	}
}
