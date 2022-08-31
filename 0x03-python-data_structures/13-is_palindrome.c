#include "lists.h"

/**
 * reverse_listint - Reverses a singly-linked listint_t list.
 * @head: pointer to the head node of the linked list.
 *
 * Return: pointer to the head of the reversed list.
 */
listint_t *reverse_list(listint_t **head)
{
	listint_t *node = *head, *next, *prev = NULL;

	while (node)
	{
		next = node->next;
		node->next = prev;
		prev = node;
		node = next;
	}

	*head = prev;
	return (*head);
}


/**
 * is_palindrome - function that checks if a singly linked list
 * is palindrome.
 * @head: pointer to pointer to head of the list.
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome.
 */
int is_palindrome(listint_t **head)
{
	listint_t *tmp, *rev, *mid;
	size_t size = 1, i;

	if (*head == NULLn || (*head)->next == NULL)
		return (1);

	tmp = *head;
	/* get the number of nodes in the list */
	for (i = 0; tmp->next != NULL; i++)
	{
		size++;
		tmp = tmp->next;
	}

	tmp = *head;
	for (i = 0; i < (size / 2) - 1; i++)
		tmp = tmp->next;

	if ((size % 2) == 0 && tmp->n != tmp->next->n)
		return (0);


	tmp = tmp->next->next;
	rev = reverse_list(&tmp);
	mid = rev;

	tmp = *head;
	while (rev)
	{
		if (tmp->n != rev->n)
			return (0);
		tmp = tmp->next;
		rev = rev->next;
	}

	reverse_list(&mid);

	return (1);
}

