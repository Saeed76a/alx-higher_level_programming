#include "lists.h"
#include <stdio.h>
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
    printf("%d\n", vues);
    while (self != mirror && vues > 0)
    {
        i = 0;
        mirror = *head;
        while (i < vues)
        {
            mirror = mirror->next;
            if (!mirror->next)
                break;
            i++;
        }
        if (mirror->n != self->n)
        {
            return (0);
        }
        vues--;
        self = self->next;
    }
    return (1);
}