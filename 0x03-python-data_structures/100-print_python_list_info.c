#include <stdio.h>
#include <stdlib.h>
#include <Python.h>
/**
 * print_python_list_info - Print basic info of Python lists
 * @p: PyObject of the program
 *
 * Return: Null
 */
void print_python_list_info(PyObject *p)
{
PyObject *thing;
PyListObject *list = (PyListObject *)p;
int m, size, alloc;

size = Py_SIZE(p);
allocate = list->allocated;
printf("[*] Size of the Python List = %d\n", size);
printf("[*] Allocated = %d\n", alloc);

for (m = 0; m < size; m++)
{
thing =  PyList_GetItem(p, m);
printf("Element %d: %s\n", m, Py_TYPE(item)->tp_name);
}
}
