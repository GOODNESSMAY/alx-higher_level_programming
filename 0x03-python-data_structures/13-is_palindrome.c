#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

/**
* is_palindrome - Check singly linked list if it's palindrome
* @head: The head
*
* Return: 0 if it is not a palindrome, 1 if it's palindrome
*/
int is_palindrome(listint_t **head)
{
listint_t *begin = NULL, *end = NULL;
unsigned int g = 0, len = 0, len_cyc = 0, len_list = 0;

if (head == NULL)
return (0);

if (*head == NULL)
return (1);

begin = *head;
len = listint_len(begin);
len_cyc = len * 2;
len_list = len_cyc - 2;
end = *head;

for (; g < len_cyc; g = g + 2)
{
if (begin[g].n != end[len_list].n)
return (0);

len_list = len_list - 2;
}

return (1);
}

/**
* get_nodeint_at_index - Get node from linked list
* @head: The head
* @index: The index to find in the linked list
*
* Return: The specific node of the linked list
*/
listint_t *get_nodeint_at_index(listint_t *head, unsigned int index)
{
	listint_t *new = head;
	unsigned int iter_times = 0;

	if (head)
	{
		while (new != NULL)
		{
		if (iter_times == index)
		return (new);

	new = new->next;
	++iter_times;
	}
	}

	return (NULL);
}

/**
* slistint_len - Count number of elements in linked list
* @h: The linked list to count
*
* Return: Number of element
*/
size_t listint_len(const listint_t *h)
{
	int len = 0;

	while (h != NULL)
	{
	++len;
	h = h->next;
	}

	return (len);

	}
