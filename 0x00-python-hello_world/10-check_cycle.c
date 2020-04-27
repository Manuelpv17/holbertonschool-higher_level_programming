#include "lists.h"
#include <stdio.h>

/**
 * check_cycle - Check if there is a cycle in linked list
 * @list: pointer to head of list
 * Return: 0 if there isn't a cycle. 1 if there is a cycle.
 */
int check_cycle(listint_t *list)
{
	while (list != NULL)
	{
		if (list->next >= list)
			return (1);
		list = list->next;
	}
	return (0);
}
