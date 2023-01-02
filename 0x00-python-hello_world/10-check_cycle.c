#include "lists.h"
#include <stdio.h>

/**
 * check_cycle - checks if a link has a cycle or not
 * @list: is the head of the linked list
 *
 * Return: 0 if no cycle and 1 if ther is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *temp1, *temp2, *check;
	int i;

	if (list == NULL)
	{
		return (0);
	}

	temp1 = list;

	while (temp1)
	{
		check = temp1->next;
		temp2 = list;
		i = 0;
		while (temp2)
		{
			if (check == temp2->next)
			{
				i++;
			}
			if (i > 1)
				return (1);
			temp2 = temp2->next;
		}
		temp1 = temp1->next;
	}
	return (0);
}

