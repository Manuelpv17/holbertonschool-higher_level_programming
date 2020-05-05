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
	listint_t *aux_back_head = NULL;

	if (head == NULL || *head == NULL)
		return (1);

	back_head = *head;
	while (back_head->next != NULL)
		back_head = back_head->next;

	aux_head = *head;
	while (aux_head->next != NULL)
	{
		if (aux_head->n != back_head->n)
			return (0);

		aux_back_head = back_head;
		back_head = *head;
		while (back_head->next != aux_back_head)
			back_head = back_head->next;
		aux_head = aux_head->next;
	}
	return (1);
}
