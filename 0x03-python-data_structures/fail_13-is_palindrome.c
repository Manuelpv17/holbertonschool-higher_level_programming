#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: head of list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *back_head = NULL;
	listint_t *aux_head = NULL;
	int len, i, j;

	if (*head == NULL)
		return (1);

	back_head = *head;
	for (len = 0; back_head->next != NULL; len++)
		back_head = back_head->next;
	aux_head = *head;
	for (i = 0; i < (len / 2) + 1; i++)
	{
		if (aux_head->n != back_head->n)
			return (0);

		back_head = *head;
		for (j = 0; j < len - i - 1; j++)
			back_head = back_head->next;
		aux_head = aux_head->next;
	}
	return (1);
}
