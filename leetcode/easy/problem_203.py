"""
203. Remove Linked List Elements

Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val,
and return the new head.
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    time complexity: O(n)
    space complexity: O(n)
    """
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        current = head

        while current:
            if current.next is None:
                break
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next

        if head:
            if head.val == val:
                head = head.next

        return head
