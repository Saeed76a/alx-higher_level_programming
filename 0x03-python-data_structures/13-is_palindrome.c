#include "lists.h"
/**
 * is_palindrome - look for palindrome
 * @head: point to head
 * Return: 1 if is it a palindrome
 * if is it not 0 returned
*/
// int is_palindrome(listint_t **head)
// {
//     listint_t *self = *head, *mirror = *head;
//     int vues = 0, i = 0;

//     while (mirror && mirror->next)
//     {
//         vues++;
//         mirror = mirror->next;
//     }
//     while (self != mirror)
//     {
//         i = 0;
//         mirror = self;
//         while (i < vues)
//         {
//             mirror = mirror->next;
//             i++;
//         }
//         if (mirror->n != self->n)
//             return (0);
//         vues -= 2;
//         if (mirror->next != self->next)
//             self = self->next;
//     }
//     return (1);
// }

int is_palindrome(listint_t **head)
{
    listint_t *self = *head, *mirror = *head, *prev = NULL, *nextNode = NULL;;
    int length = 0, i = 0;

    // Calculate the length of the list
    while (mirror && mirror->next)
    {
        length += 2;
        mirror = mirror->next->next;
    }

    // Adjust length if the list is odd
    if (mirror != NULL)
        length++;

    mirror = *head;

    // Traverse to the middle of the list
    for (i = 0; i < length / 2; i++)
        mirror = mirror->next;

    // Reverse the second half of the list
    while (mirror)
    {
        nextNode = mirror->next;
        mirror->next = prev;
        prev = mirror;
        mirror = nextNode;
    }

    // Compare the reversed second half with the first half
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
