#include "lists.h"

/**
 * is_palindrome - function that checks if a singly linked list
 * is palindrome.
 * @head: pointer to pointer to head of the list.
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome.
 */
int is_palindrome(listint_t **head)
{
	int i, j, k;
	int *member;
	listint_t *tmp = *head;

	if (*head == NULL)
		return (1);

	/* get the number of nodes in the list */
	for (i = 1; tmp->next != NULL; i++)
		tmp = tmp->next;

	member = malloc(sizeof(int) * i);

	/* fill the array with the n member of each node */
	tmp = *head;
	for (j = 0; j < i; j++)
	{
		member[j] = tmp->n;
		tmp = tmp->next;
	}

	k = j;
	/*compare both end of array to test for palindromeness */
	for (i = 0; i <= j; i++)
	{
		for (j = k; j >= i; j--)
		{
			if (member[i] == member[j] && i == j)
				return (1);
		}
	}

	return (0);
}

