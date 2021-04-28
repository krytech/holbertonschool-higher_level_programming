#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to the head of the linked list
 * @number: number to insert in the linked list
 * Return: address of the new new, otherwise NULL if failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *ph = *head;

	if ((!ph) || ph->n > number)
	{
		new = malloc(sizeof(listint_t));
		if (!new)
			return (NULL);

		new->n = number;
		new->next = *head;
		*head = new;
		return (*head);
	}
	while (ph)
	{
		if ((!ph->next || ph->next->n > number))
		{
			new = malloc(sizeof(listint_t));
			if (!new)
				return (NULL);
			new->n = number;
			new->next = ph->next;
			ph->next = new;
			return (new);
		}
		ph = ph->next;
	}
	return (NULL);
}
