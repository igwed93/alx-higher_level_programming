#include "lists.h"
#include <string.h>

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
	k = 0;
	tmp = *head;

	/* fill the array with the n member of each node */
	while (k < i)
	{
		member[k] = tmp->n;
		tmp = tmp->next;
		k++;
	}

	k = 0;
	printf("\n");

	while (k < i)
	{
		printf("%d ", member[k]);
		k++;
	}

	/*compare both end of array to test for palindromeness */
	k = i - 1;
	j = 0;
	tmp = *head;
	printf("\n");
	while (k >= 0)
	{
		if (member[k] == tmp->n)
		{
			printf("member[%d]: %d and tmp->%d: %d\n", k, member[k], j, tmp->n);
		}
		else
		{
			return (0);
		}
		j++;
		tmp = tmp->next;
		k--;
		continue;
	}

	return (1);
}

