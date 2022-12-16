"""
147. Insertion Sort List

Given the head of a singly linked list, sort the list using insertion sort, and return the sorted list's head.

The steps of the insertion sort algorithm:

    Insertion sort iterates, consuming one input element each repetition and growing a sorted output list.
    At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the
    sorted list and inserts it there.
    It repeats until no input elements remain.

The following is a graphical example of the insertion sort algorithm. The partially sorted list (black) initially
contains only the first element in the list. One element (red) is removed from the input data and inserted in-place
into the sorted list with each iteration.

Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class BadSolution:

    def create_List(self, lst):
        current = dummy = ListNode(lst[0])
        for e in lst[1:]:
            if e is None:
                current.next = None
            else:
                current.next = ListNode(e)
                current = current.next
        return dummy

    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        lst = list()

        while current:
            lst.append(current.val)
            current = current.next

        for i in range(1, len(lst)):
            for j in range(i, 0, -1):
                a, b = lst[j], lst[j - 1]
                if a < b:
                    lst.insert(j - 1, lst.pop(j))

        lst.append(None)

        # Create the linked list
        new_list = self.create_List(lst)

        return new_list


class BuggySolution:

    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(None, head)
        sorted_list = dummy.next
        prev, current = dummy, dummy.next

        cnt = 0
        while current.next:
            cnt += 1
            prev, current = current, current.next

            if current.val >= prev.val:
                continue

            for i in range(cnt):
                start_over = sorted_list
                if current.val < start_over.val:
                    prev.next = current.next
                    current.next = start_over.next
                    start_over.next = current
                    break

        return sorted_list
