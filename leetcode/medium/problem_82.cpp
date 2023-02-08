/*
82. Remove Duplicates from Sorted List II

Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

Example 1:

Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]

Example 2:

Input: head = [1,1,1,2,3]
Output: [2,3]

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
    ListNode* deleteDuplicates(ListNode* head) {

        if (head == nullptr) return head;
        if (head->next == nullptr) return head;

        ListNode* curr = head->next;
        ListNode* prev = head;

        bool rm_head = head->val == head->next->val;

        while(true){
            if (curr == nullptr) break;
            if (curr->next == nullptr) break;

            // std::cout << curr->val << std::endl;

            if (curr->val == curr->next->val){
                int dupl = curr->val;
                while(curr->val == dupl){
                    prev->next = curr->next;
                    curr = curr->next;
                    if (prev->next == nullptr) break;
                }
            } else {
                curr = curr->next;
                prev = prev->next;
            }

        }

        if (head->next != nullptr && head->val == head->next->val) return head->next->next;
        if (rm_head) head = head->next;

    return head;
    }
};
