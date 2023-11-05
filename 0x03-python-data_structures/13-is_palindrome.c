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
	listint_t *first;
	lisint_t *last;
	int count = 0;

	first = head;
	last = NULL;

	/*find last node*/
	while (last-> NULL)
		last = last->next;

	while (first != Null)
	{
		if (first->n == last->n)
		{
			count++;
			printf("match!\n");
		}
		else
		{
			printf("not a match!\n");
			break
		}
		first = first->next;
		last = 
	}


	/*loop */
	/*check if first node value/ addree is the same*/
	/*enter loop and check next node*/
	/* if not, not palindrome*/
}
