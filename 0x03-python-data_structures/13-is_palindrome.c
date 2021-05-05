#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: head of the list
 * Return: 0 if not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *ph = *head;
	unsigned int size = 0, i = 0;
	int data[10240];

	if (!head) /* no list is not a pal */
		return (0);

	if (!*head) /* empty list is a pal */
		return (1);

	while (ph) /* finds size of list */
	{
		ph = ph->next;
		size += 1;
	}

	ph = *head;
	while (ph) /* saves numbers to compare */
	{
		data[i++] = ph->n;
		ph = ph->next;
	}

	/* compare the start and end of the list until the mid point */
	for (i = 0; i <= (size / 2); i++)
	{
		if (data[i] != data[size - i - 1])
			return (0);
	}
	return (1);
}
