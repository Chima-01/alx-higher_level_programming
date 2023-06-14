#include "lists.h"

/**
 * is_palindrome - This function checks if a
 * singly linked list is a palindrome.
 * @head: head of list
 * Return: 1 if palindrome else 0
 */

int is_palindrome(listint_t **head)
{
	listint_t *reverse, *current, *rev = *head;
	size_t count, i = 0;

	if (head == NULL || (*head)->next == NULL)
		return (1);

	count = listint_len(*head);
	reverse = reverse_listint(&rev);
	current = *head;

	while ((current && reverse) && i < (count / 2))
	{
		if (current->n != reverse->n)
			return (0);

		printf("reverse %d\n", reverse->n);
		printf("current %d\n", current->n);
		current = current->next;
		reverse = reverse->next;
		i++;
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
	listint_t *current = NULL;

	if (head == NULL)
		return (NULL);

	current = *head;

	while (current != NULL)
	{
		fwd = current->next;
		current->next = prev;
		prev = current;
		current = fwd;
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

/**int is_palindrome(listint_t **head)
{
    if (*head == NULL || (*head)->next == NULL) {
        return 1;  // An empty list or a list with a single node is considered a palindrome
    }

    // Find the middle of the linked list
    listint_t *slow = *head;
    listint_t *fast = *head;
    while (fast != NULL && fast->next != NULL) {
        slow = slow->next;
        fast = fast->next->next;
    }

    // Reverse the second half of the linked list
   listint_t *prev = NULL;
    listint_t *current = slow;
    listint_t *next = NULL;

    while (current != NULL) {
        next = current->next;   // Store the next node
        current->next = prev;   // Reverse the pointer of the current node
        prev = current;         // Move prev and current one step forward
        current = next;
    }

    listint_t 

    // Compare the first half with the reversed second half
    listint_t *firstHalf = *head;
    listint_t *secondHalf = prev;

    while (firstHalf != NULL && secondHalf != NULL) {
        if (firstHalf->n != secondHalf->n) {
            return 0;  // Not a palindrome
        }
        firstHalf = firstHalf->next;
        secondHalf = secondHalf->next;
    }

    return 1;  // Palindrome
}
*/
