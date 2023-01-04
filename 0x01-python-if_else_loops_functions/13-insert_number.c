#include "lists.h"

/**
 * insert_node - inserts node in a sorted list
 * @head: is a pointer pointing to the head of the node
 * @number: is the interger value to be added
 *
 * Return: addtess of the new link
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp1, *temp2, *current;
	int flag = 0;

	temp1 = *head;
	if (*head == NULL)
		return (NULL);

	while (temp1)
	{
		if (temp1->n <= number && number <= temp1->next->n)
		{
			flag = 1;
			break;
		}
		temp1 = temp1->next;
	}
	if (flag == 0)
	{
		temp1 = *head;
		if ((temp1->n > temp1->next->n && temp1->n < number) ||
				(temp1->n < temp1->next->n && temp1->n > number))
			flag = 1;
	}
	if (flag == 0)
	{
		temp1 = *head;
		while (temp1)
			temp1 = temp1->next;
	}

	temp2 = malloc(sizeof(listint_t));
	if (temp2 == NULL)
		return (NULL);
	temp2->n = number;
	temp2->next = NULL;
	current = temp1->next;
	temp1->next = temp2;
	temp2->next = current;

	return (*head);
}

