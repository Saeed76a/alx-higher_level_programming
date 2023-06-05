#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: a list of nodes
 * Return: 0 if is safe
 * 1 returned if is unsafe
 */
int check_cycle(listint_t *list)
{
	listint_t *current, *tmp;

	if (!list)
		return (0);
	current = list;
	while (current)
	{
		tmp = list;
		if (current == current->next)
			return (1);
		while (tmp != current)
		{
			if (current->next == tmp)
				return (1);
			tmp = tmp->next;
		}
		current = current->next;
	}
	return (0);
}
