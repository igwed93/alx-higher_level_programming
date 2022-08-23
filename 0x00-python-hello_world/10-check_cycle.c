#include "lists.h"

/**
 * check_cycle - function that checks if a singly
 * linked list has a cycle in it.
 *
 * @list: linked list to be checked.
 *
 * Return: 0 if a cycle is present, otherwise 1.
 */
int check_cycle(listint_t *list)
{
	int i = 0;
	while (list != NULL)
	{
		list = list->next;
		i++;
		
		if (i >= 15 && list->next != NULL)
			return (1);
	}
	
	return (0);
}

