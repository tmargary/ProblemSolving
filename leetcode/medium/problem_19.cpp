/*
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:

Input: head = [1], n = 1
Output: []

Example 3:

Input: head = [1,2], n = 1
Output: [1]

*/


// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* curr = head;

        int length = 0;
        while (curr != nullptr) {
            curr = curr->next;
            length++;
        }

        int index = length-n;

        curr = head;
        if (curr->next == nullptr || index == 0) return curr->next;

        for (int i{}; i < index; ++i) {
            if (curr->next == nullptr) break;
            if (i == index - 1) {
                curr->next = curr->next->next;
            }
            curr = curr->next;
        }
        return head;
    }
};
