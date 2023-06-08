#include "lists.h"

/**
 * check_cycle - This function checks if a singly linked list
 * has a cycle in it.
 * @list: head of node
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *current;

	if (list == NULL)
		return (0);

	current = list;
	while (current != NULL)
	{
		current = current->next;
		if (list == current)
			return (1);
	}
		return (0);
}
