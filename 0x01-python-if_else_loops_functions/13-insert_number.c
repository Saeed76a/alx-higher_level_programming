#include "lists.h"
#include <stdlib.h>

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = malloc(sizeof(listint_t)), *root = *head;
	listint_t *current = root, *prev = root;

	if (!new)
		return(NULL);
	new->num = number;
	if (!*head)
	{
		new->next = NULL;
		*head = new;
		return (*head);
	}
	if (new->num <= root->num)
	{
		new->next = root;
		*head = new;
		return(*head);
	}
	    
	while (current)
	{
		if (new->num > current->num && !current->next)
		{
			current->next = new;
			new->next = NULL;
			return(*head);
		}
		if (new->num <= current->num)
		{
			prev->next = new;
			new->next = current;
			return(*head);
		}
		prev = current;
		 current = current->next;
	}
}
