#include "lists.h"

int is_palindrome(listint_t **head)
{
	listint_t *slow;
	listint_t *fast;
	listint_t *second_half;
	listint_t *prev;
	listint_t *current;
	listint_t *next;

	if (head == NULL || *head == NULL || (*head)->next == NULL)
		return (1);

	slow = *head;
	fast = *head;

	while (fast->next != NULL && fast->next->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
	}

	second_half = slow->next;
	prev = NULL;

	while (second_half != NULL)
	{
		next = second_half->next;
		second_half->next = prev;
		prev = second_half;
		second_half = next;
	}

	current = *head;
	second_half = prev;

	while (second_half != NULL)
	{
		if (current->n != second_half->n)
			return (0);

		current = current->next;
		second_half = second_half->next;
	}

	return (1);
}
