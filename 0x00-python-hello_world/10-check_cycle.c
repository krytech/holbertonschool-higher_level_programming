#include "lists.h"

/**
 * check_cycle - checkes a linked list to find a loop
 * @list: begining of the linked list
 * Return: 1 if there is a loop, otherwise 0 if no loop
 */

int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	/* goes through the list until the end */
	while (slow && fast && fast->next)
	{
		/* slow moves ahead one, fast twice, and compares */
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast) /* match found, returns 1 */
			return (1);
	}
	return (0); /* no match, return 0 */
}
