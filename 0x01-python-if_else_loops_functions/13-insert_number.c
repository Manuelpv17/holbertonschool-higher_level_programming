#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: double pointer to head
 * @number: value of the new element
 * Return: pointer to the new element
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *aux = *head;
	listint_t *new = NULL;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (*head == NULL)
	{
		*head = new;
		return (new);
	}
	else if (aux->n > number)
	{
		*head = new;
		new->next = aux;
		return (new);
	}

	while (aux->next != NULL && aux->next->n < number)
		aux = aux->next;

	new->next = aux->next;
	aux->next = new;
	return (new);
}
