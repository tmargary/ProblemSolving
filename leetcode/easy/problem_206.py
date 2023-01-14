"""
206. Reverse Linked List

Given the head of a singly linked list, reverse the list, and return the reversed list.
"""


from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MySolution:

    def create_List(self, lst):
        current = dummy = ListNode(lst[0])
        for e in lst[1:]:
            if e is None:
                current.next = None
            else:
                current.next = ListNode(e)
                current = current.next
        return dummy

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        reverse_val = list()

        while current:
            reverse_val.append(current.val)
            current = current.next

        reverse_val = reverse_val[::-1]

        if len(reverse_val) == 0:
            return None

        reverse_val.append(None)

        # Create the linked list
        new_list = self.create_List(reverse_val)

        return new_list


class BetterSolution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        reverse_head = None

        while current:
            next = current.next  # remember the next node
            current.next = reverse_head  # asign the head of the reverse list (starting None)
            reverse_head = current  # point the reverse head to the current node
            current = next  # asign the initial next node to current

        return reverse_head
