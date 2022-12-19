"""
617. Merge Two Binary Trees

You are given two binary trees root1 and root2.

Imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others
are not. You need to merge the two trees into a new binary tree. The merge rule is that if two nodes overlap, then sum
node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of the new
tree.

Return the merged tree.

Note: The merging process must start from the root nodes of both trees.

Example 1:

Input: root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]
Output: [3,4,5,5,4,null,7]
Example 2:

Input: root1 = [1], root2 = [1,2]
Output: [2,2]
"""
import copy


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:

        if t1 and not t2:
            return t1
        if not t1 and t2:
            return t2

        t3 = copy.deepcopy(t1)
        stack = [[t3, t2]]

        while stack:
            cur = stack.pop()

            # if either the left and right does not exist, start over, else calc the sum
            if cur[0] == None or cur[1] == None:
                continue
            else:
                cur[0].val += cur[1].val

            # if left's left doesn't exist, assign the right's left node
            if cur[0].left == None:
                cur[0].left = cur[1].left
            else:
                stack.append([cur[0].left, cur[1].left])

            # if left's left doesn't exist, assign the right's right node
            if cur[0].right == None:
                cur[0].right = cur[1].right
            else:
                stack.append([cur[0].right, cur[1].right])

        return t3
