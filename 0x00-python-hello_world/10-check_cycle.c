#include "lists.h"
/**
 * check_cycle - check for loop in LL
 * @list: head of linked list
 *
 * Description - check for loops in LL
 * Return: 1 if there is a cycle, 0 if there is no cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;
	if (!list)
	{
		return (0);
	}
	slow = list;
	fast = list->next;
	while (fast && slow && fast->next)
	{
		if (slow == fast)
		{
			return (1);
		}
		slow = slow->next;
		fast = fast->next->next;
	}
	return (0);
}
