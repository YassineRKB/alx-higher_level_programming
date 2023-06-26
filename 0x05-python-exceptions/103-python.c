#include <Python.c>

/**
 * print_python_list - function to print basic info about python lists
 * @p: pointer to python pyobject
 * Return: void
*/
void print_python_list(PyObject *p)
{
	const char *pytype;
	int allocated, s, i = 0;
	PyVarObject *pyvar = (PyVarObject *) p;
	PyListObject *pylist = (PyListObject *) p;

	fflush(stdout);
	allocated = pylist->allocated;
	s = pyvar->ob_size;
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", s);
	printf("[*] Allocated = %d\n", allocated);
	while (i < s)
	{
		pytype = ((PyListObject *)p)->ob_item[i]->ob_type->tp_name;
		printf("Element %d: %s\n", i, pytype);
		if (!strcmp(pytype, "bytes"))
			print_python_bytes(pylist->ob_item[i]);
		i++;
	}
}
/**
 * print_python_bytes - function to print basic infor about bytes obj
 * @p: pointer to python pyobject
 * Return: void
*/
void print_python_bytes(PyObject *p)
{
	char *string = ((PyBytesObject *)p)->ob_sval;
	long int i, size = ((PyVarObject *)p)->ob_size;

	fflush(stdout);
	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", string);
	if (((PyVarObject *)p)->ob_size < 10)
		size = ((PyVarObject *)p)->ob_size + 1;
	else
		size = 10;

	printf("  first %ld bytes: ", size);
	for (i = 0; i < size; i++)
	{
		if (i == size - 1)
			printf("%02hhx%s", string[i], "\n");
		else
			printf("%02hhx%s", string[i], " ");
	}
}
/**
 * print_python_float - function to print python float
 * @p: a float PyObject
*/
void print_python_float(PyObject *p)
{
	char *buffer = NULL;
	double value;
	PyFloatObject *fobj = (PyFloatObject *)p;

	fflush(stdout);
	printf("[.] float object info\n");
	if (strcmp(p->ob_type->tp_name, "float") != 0)
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	value = fobj->ob_fval;
	buffer = PyOs_double_to_string(value, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	print("  value: %s\n", buffer);

}
