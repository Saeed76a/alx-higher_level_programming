#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = malloc(sizeof(listint_t)), *root = *head;
	listint_t *current = root, *prev = root;

	new->n = number;
	if (!new)
		return (NULL);
	if (!*head)
	{
		new->next = NULL;
		*head = new;
		return (*head);
	}
	if (new->n <= root->n)
	{
		new->next = root;
		*head = new;
		return(*head);
	}
	    
	while (current)
	{
		if (new->n > current->n && !current->next)
		{
			current->next = new;
			new->next = NULL;
			return(*head);
		}
		if (new->n <= current->n)
		{
			prev->next = new;
			new->next = current;
			return(*head);
		}
		prev = current;
		current = current->next;
	}
	return(*head);
}
