#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if function is palindrome
 * @head: pointer to the head
 * Return: 1 if palindrome, 0 otherwise
 */

int is_palindrome(listint_t **head)
{
	listint_t *copy_head;
	listint_t *first, *last, *current;
	/*make a copy of the head*/
	copy_head = *head;
	/*main loop check if first and are equal*/
	while (copy_head != NULL)
	{
		/*find first elemnet*/
		first = copy_head;
		/*find last element*/
		last = copy_head;
		current = copy_head;
		while (current->next != NULL)
		{
			current = current->next;
		}
		last = current;
		/*compare element*/
		if (first->n == last->n)
		{
		/*update first element to second element*/
			first = first->next;
		/*update last element to second last element*/
			current = copy_head;
			while (current->next->next != NULL)
			{
				current = current->next;
			}
			last = current;
			last->next = NULL;
			copy_head = copy_head->next;
		/*making a secons last node point to NULL*/
		}
		else
		{
			return (0);
		}
	/*if not break from loop and return 0*/
	}
	return (1);
}
