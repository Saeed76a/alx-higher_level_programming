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

    if (!self)
        return (1);
    while (mirror->next)
    {
        vues++;
        mirror = mirror->next;
    }
    while (self != mirror && mirror->next != self)
    {
        i = 0;
        mirror = self;
        while (i < vues)
        {
            mirror = mirror->next;
            if (!mirror->next)
                break;
            i++;
        }
        if (mirror->n != self->n)
            return (0);
        vues -= 2;        
        self = self->next;
    }
    return (1);
}