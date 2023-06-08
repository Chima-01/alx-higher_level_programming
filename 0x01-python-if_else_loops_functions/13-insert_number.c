#include "lists.h"

/**
 * insert_node - This fuction inserts a ne node into
 * sorted linked list
 * @head: head of the list
 * @number: value of new node
 * Return: address of new node or null
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *ptr;
	listint_t *node;

	ptr = malloc(sizeof(listint_t));
	if (!ptr)
		return (NULL);

	ptr->n = number;
	node = *head;
	while (node->next && node->next->n < number)
	{
		node = node->next;
	}
	ptr->next = node->next;
	node->next = ptr;

		return (ptr);
}
