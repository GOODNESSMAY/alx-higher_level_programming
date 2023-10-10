#include "Python.h"
#include "object.h"
#include "listobject.h"
/**
 * print_python_list_info - Print basic info of Python lists
 * @p: PyObject of the program
 *
 * Return: Null
 */
void print_python_list_info(PyObject *p)
{
PyListObject *list = (PyListObject *)p;
long int size = PyList_Size(p);
int m;

printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (m = 0; m < size; m++)
		printf("Element %d: %s\n", m, Py_TYPE(list->ob_item[m])->tp_name);
}
