#include "lists.h"
/**
 * is_palindrome - look for palindrome
 * @head: point to head
 * Return: 1 if is it a palindrome
 * if is it not 0 returned
*/
int is_palindrome(listint_t **head)
{
    listint_t *self = *head, *mirror = *head;
    int vues = 0, i = 0;

    while (mirror && mirror->next)
    {
        vues++;
        mirror = mirror->next;
    }
    while (self != mirror)
    {
        i = 0;
        mirror = self;
        while (i < vues)
        {
            mirror = mirror->next;
            i++;
        }
        if (mirror->n != self->n)
            return (0);
        vues -= 2;
        if (mirror->next != self->next)
            self = self->next;
    }
    return (1);
}