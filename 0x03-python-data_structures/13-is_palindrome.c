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
	listint_t *copy_head, *first, *last, *current;
	/*make a copy of the head*/
	copy_head = *head;
	/*main loop check if first and are equal*/
	while (copy_head != NULL)
	{
		/*find first elemnet*/
		first = copy_head;
		/*find last element*/
		current = copy_head;
		last = NULL;
		while (current->next != NULL)
		{
			last = current;
			current = current->next;
		}
		/*compare element*/
		if ((first->n == last->n) && first != last)
		{
			return (0);
		}
		/*skip middle for odd palindromes*/
		if (first == current)
			break;
		if (last != NULL)
			last->next = NULL;
		copy_head = first->next;
	}
	return (1);
}
