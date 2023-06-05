#include "lists.h"
/**
 * check_cycle - function to check if linked list has loop
 * @list: first node of linked list
 * Return: 0 if there is no cycle, else 1
*/
int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list;

	if (!list)
		return (0);
	for (; fast && fast->next;)
	{
		fast = fast->next->next;
		slow = slow->next;
		if (fast == slow)
		{
			return (1);
		}
	}
	return (0);
}
