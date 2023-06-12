#include "lists.h"
/**
 * is_palindrome - func to check if list is palindrome
 * @head: header of the linked list
 * Return: 1 if palindrome or 0 otherwise
*/
int is_palindrome(listint_t **head)
{
	listint_t *llist = *head, *tlist = *head, *p = NULL, *t = NULL;

	if (!head)
		return (0);
	if (!llist)
		return (1);
	
	for (; llist && llist->next;p = t->next)
	{
		llist = llist->next->next;
		t = tlist;
		tlist = tlist->next;
		t->next = p;
	}
	
	if (llist)
		tlist = tlist->next;

	for (; tlist && p; tlist = tlist->next, llist = llist->next)
	{
		if (tlist->n != p->n)
		{
			return (0);
		}
	}
	return (1);
}
