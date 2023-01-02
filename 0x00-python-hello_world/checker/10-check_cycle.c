#include "lists.h"
#include <stdio.h>

/**
 * check_cycle - checks if a link has a cycle or not
 * @list: is the head of the linked list
 *
 * Return: 0 if there is no cycle and 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *temp1, *temp2;

	if (list == NULL)
	{
		return (0);
	}

	temp1 = list;
	temp2 = list;

	while (temp1 && temp2 && temp2->next)
	{
		temp1 = temp1->next;
		temp2 = temp2->next->next;
		
		if (temp1 == temp2)
		{
			return (1);
		}
	}
	return (0);
}

