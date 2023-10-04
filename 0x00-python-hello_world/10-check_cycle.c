#include "lists.h"

/**
* check_cycle - funct to check if singly linked list has a cycle inside.
* @list: pointer to beginning of node
* Return: void if no cycle || 1 if cycle exists
*/
int check_cycle(listint_t *list)
{
	listint_t *slug = list;
	listint_t *may = list;

	if (!list)
		return (0);

	while (slug && may && may->next)
	{
		slug = slug->next;
		may = may->next->next;
		if (slug == may)
			return (1);
	}

	return (0);
}

