#include "lists.h"

/**
 * print_dlistint -  prints all the elements of a dlistint_t list
 * @h: head/ pointer to first node
 * Return: number of nodes
 */

size_t print_dlistint(const dlistint_t *h)
{
	int count = 0;

	while (h != NULL)
	{
		h = h->next;
		count++;
	}
	return (count);
}
