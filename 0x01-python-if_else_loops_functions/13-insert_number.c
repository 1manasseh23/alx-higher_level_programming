#include <stdlib.h>
#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *n_node = malloc(sizeof(listint_t));
	listint_t *current;

	if (n_node == NULL)
	{
		return (NULL);
	}
	n_node->n = number;
	n_node->next = NULL;

	if (*head == NULL || number < (*head)->n)
	{
		n_node->next = *head;
		*head = n_node;
		return (n_node);
	}

	current = *head;
	while (current->next != NULL && current->next->n < number)
	{
		current = current->next;
	}

	n_node->next = current->next;
	current->next = n_node;

	return (n_node);
}
