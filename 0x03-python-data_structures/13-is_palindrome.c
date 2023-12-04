#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
int is_palindrome(listint_t **head)
{
	listint_t *saver = *head;
	int count = 0, j = 0;
	int array[10000];

	if (!*head || !((*head)->next))
		return (1);
	while (saver != NULL)
	{
		array[count] = saver->n;
		count++;
		saver = saver->next;
	}
	count--;
	saver = *head;

	while (saver != NULL)
	{
		if (saver->n != array[count - j])
			return(0);

		j++;
		saver = saver->next;
	}
	return(1);
}
