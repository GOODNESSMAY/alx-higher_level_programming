#include <stdio.h>
#include <stdlib.h>
#include <Python.h>
#include <object.h>
#include <listobject.h>
/**
 * print_python_list_info - Print basic info of Python lists
 * @p: PyObject of the program
 *
 * Return: Null
 */
void print_python_list_info(PyObject *p)
{
PyObject *item;
PyListObject *list = (PyListObject *)p;
long int m, size, alloc;

size = Py_SIZE(p);
alloc = list->allocated;
printf("[*] Size of the Python List = %ld\n", size);
printf("[*] Allocated = %ld\n", alloc);

for (m = 0; m < size; m++)
{
item =  PyList_GetItem(p, m);
printf("Element %ld: %s\n", m, Py_TYPE(item)->tp_name);
}
}
