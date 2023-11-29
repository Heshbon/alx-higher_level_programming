#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - a function that inserts a number into a sorted singly-linked list
 * @head: pointer of the linked list
 * @number: the number to insert
 * Return: the address of the new node, or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *p = *head, *b;

	b = malloc(sizeof(listint_t));
	if (b == NULL)
		return (NULL);
	b->n = number;

	if (p == NULL || p->n >= number)
	{
		b->next = p;
		*head = b;
		return (b);
	}
	while (p && p->next && p->next->n < number)
		p = p->next;
	b->next = p->next;
	p->next = b;

	return (b);
}
