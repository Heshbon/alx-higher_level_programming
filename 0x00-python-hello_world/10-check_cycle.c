#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle
 * @list: Singly-linked list
 * Return: 0 if there is no cycle
 * 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *c;
	listint_t *b;

	if (list == NULL || list->next == NULL)
		return (0);

	c = list->next;
	b = list->next->next;

	while (c && b && b->next)
	{
		if (c == b)
			return (1);

		c = c->next;
		b = b->next->next;
	}
	return (0);
}
