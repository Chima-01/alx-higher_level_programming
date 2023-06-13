#include "lists.h"

/**
 * is_palindrome - This function checks if a
 * singly linked list is a palindrome.
 * @head: head of list
 * Return: 1 if palindrome else 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *reverse, *current;
	size_t count, i = 0;

	if (*head == NULL || head == NULL)
		return (1);

	count = listint_len(*head);
	reverse = reverse_listint(head);
	current = *head;

	while (current != NULL && i < (count / 2))
	{
		if (current->n != reverse->n)
			return (0);

		current = current->next;
		reverse = reverse->next;
	}
			return (1);
}


/**
 * reverse_listint - This function reverses a listint_t linked list.
 * @head: pointer to head node
 * Return: a pointer to the first node of the reversed list
 */

listint_t *reverse_listint(listint_t **head)
{
	listint_t *fwd = NULL;
	listint_t *prev = NULL;

	if (head == NULL)
		return (NULL);

	while (*head)
	{
		fwd = (*head)->next;
		(*head)->next = prev;
		prev = *head;
		*head = fwd;
	}
		*head = prev;
		return (prev);
}


/**
 * listint_len - A function that returns the number of elements in a linked
 * listint_t list.
 * @h: pointer to elements in listint_t
 * Return: number of nodes
 */

size_t listint_len(listint_t *h)
{
	unsigned int count = 0;

	while (h != NULL)
	{
		count++;
		h = h->next;
	}
		return (count);
}
