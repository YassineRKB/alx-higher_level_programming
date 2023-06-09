#include "lists.h"
/**
 * is_palindrome - func to check if list is palindrome
 * @head: header of the linked list
 * Return: 1 if palindrome or 0 otherwise
*/
int is_palindrome(listint_t **head)
{
	listint_t *lenlist = *head, *list = *head;
	unsigned long int data[10000], len = 0, i = 0;

	if (!head)
		return (0);
	if (!list)
		return (1);
	len = calclen(lenlist);
	for (; list; i++, list = list->next)
		data[i] = list->n;
	for (i = 0; i <= (len / 2); i++)
		if (data[i] != data[len - i - 1])
			return (0);
	return (1);
}
int calclen(listint_t *list)
{
	int len;

	for (len = 0; list; len++)
		list = list->next;
	return len;
}
