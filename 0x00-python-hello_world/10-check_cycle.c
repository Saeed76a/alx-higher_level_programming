#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: a list of nodes
 * Return: 0 if is safe
 * 1 returned if is unsafe
 */
int check_cycle(listint_t *list)
{
	listint_t *current, *tmp = list;

	if (!list)
		return (0);
	current = list;
	while (current && tmp)
	{
		current = current->next;
		if (!current)
			return (0);
		if (!(tmp->next))
			return (0);
		tmp = tmp->next->next;
		if (tmp == current)
			return (1);
	}
	return (0);
}
