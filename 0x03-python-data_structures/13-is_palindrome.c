#include "lists.h"
/**
 * is_palindrome - look for palindrome
 * @head: point to head
 * Return: 1 if is it a palindrome
 * if is it not 0 returned
*/

int is_palindrome(listint_t **head)
{
    listint_t *self = *head, *mirror = *head, *prev = NULL, *nextNode = NULL;
    int length = 0, i = 0;

    while (mirror && mirror->next)
    {
        length += 2;
        mirror = mirror->next->next;
    }
    if (mirror != NULL)
        length++;
    mirror = *head;
    for (i = 0; i < length / 2; i++)
        mirror = mirror->next;
    while (mirror)
    {
        nextNode = mirror->next;
        mirror->next = prev;
        prev = mirror;
        mirror = nextNode;
    }    
    mirror = prev;
    while (mirror)
    {
        if (self->n != mirror->n)
            return (0);
        self = self->next;
        mirror = mirror->next;
    }
    return (1);
}
