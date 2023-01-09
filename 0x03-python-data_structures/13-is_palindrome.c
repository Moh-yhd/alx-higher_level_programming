#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

int is_palindrome(listint_t **head)
{
	listint_t *temp;
	int *list_elem;
	unsigned int i;

	if (*head == NULL || head == NULL)
		return (1);
	temp = *head;
	while (temp->next)
	{
		i++;
		temp = temp->next;
	}

	list_elem = malloc(sizeof(int) * i);

	temp = *head;
	i = 0;
	while (temp)
	{
		list_elem[i] = temp->n;
		temp = temp->next;
		i += 1;
	}
	temp = *head;
	i = i - 1;
	while (temp->next)
	{
		if (list_elem[i] != temp->n)
			return (0);
		temp = temp->next;
		i -= 1;
	}

	return (1);
}
