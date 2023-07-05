#include <Python.h>
/**
 * print_python_string - func to print a python string
 * @p: string
 * Return: VOID
*/
void print_python_string(PyObject *p)
{
	long int length = 0;

	fflush(stdout);
	printf("[.] string object info\n");
	if (!PyUnicode_CheckExact(p))
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}
	if (PyUnicode_IS_ASCII(p))
		printf("  type: compact ascii\n");
	else
		printf("  type: compact unicode object\n");
	length = PyUnicode_GET_LENGTH(p);
	printf("  length: %ld\n", length);
	printf("  value: %S\n", PyUnicode_AsWideCharString(p, NULL));
}
