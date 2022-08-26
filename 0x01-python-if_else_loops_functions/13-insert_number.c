#include "lists.h"

/**
 * insert_node - function that inserts a number into a sorted
 * singly linked list.
 * @head: pointer to the head of the linked list.
 * @number: number to insert at the appropriate position in the
 * sorted list.
 *
 * Return: the address of the new node or NULL if it failed.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = malloc(sizeof(listint_t));
	listint_t *tmp = *head;

	if (!head)
		return (NULL);

	/* verify if malloc failed */
	if (!new)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (*head == NULL)
		*head = new;
	else if (number < tmp->n)
	{
		new->next = tmp;
		*head = new;
		return (*head);
	}
	else
	{
		while (tmp->next)
		{
			if (number > tmp->next->n)
				tmp = tmp->next;
			else
				break;
		}
		new->next = tmp->next;
		tmp->next = new;
	}

	return (new);
}
