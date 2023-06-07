#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - function to insert node in a linked list
 * @head: pointer to the head node of the linked list
 * @number: number of the new node to be inserted
 * Return: pointer to address of the new node.
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *list = *head, *nlist;
	int i = 0;

	if(!list)
	{
		add_nodeint_end(head, number);
		return (*head);
	}

	while (list && list->next)
	{
		if (!list->next->next || number <= list->next->n)
		{
			if (!list->next->next && number > list->next->n)
			{
				list = list->next;
			}
			nlist = malloc(sizeof(listint_t));
			if (!nlist)
				return (NULL);
			nlist->n = number;
			if (i != 0)
			{
				nlist->next = list->next;
				list->next = nlist;
			}
			if (i == 0)
			{
				nlist->next = *head;
				*head = nlist;
			}
			return (nlist);
		}
		list = list->next;
		i++;
	}
	return (NULL);
}