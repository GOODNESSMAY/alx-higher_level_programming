#include "lists.h"

/**
* insert_node - Insert num into a sorted singly-linked list.
* @head: A pointer the head.
* @number: The num to insert.
*
* Return: If the function fails - NULL.
* Otherwise - return pointer to  new node.
*/
listint_t *insert_node(listint_t **head, int number)
{
listint_t *node = *head, *may;

	may = malloc(sizeof(listint_t));
	if (may == NULL)
		return (NULL);
	may->n = number;

	if (node == NULL || node->n >= number)
	{
		may->next = node;
		*head = may;
		return (may);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;

	may->next = node->next;
	node->next = may;

	return (may);
}

