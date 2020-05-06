#include "lists.h"

int aux_func(listint_t **, listint_t *);

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: head of list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	return (aux_func(head, *head));
}

int aux_func(listint_t **head, listint_t *b_head)
{
	if (b_head->next != NULL)
		aux_func(head, b_head->next);
	if ((*head)->n == b_head->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}
