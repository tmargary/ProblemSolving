"""
94. Binary Tree Inorder Traversal

Given the root of a binary tree, return the inorder traversal of its nodes' values.
"""
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:

    results = list()

    def rec(self, root):
        if root:
            self.rec(root.left)
            self.results.append(root.val)
            self.rec(root.right)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.rec(root)
        return self.results


class Solution2:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        if root is None:
            return list()

        stack = [[root, True]]
        results = list()

        while True:
            if len(stack) == 0:
                break
            root, go_left = stack[-1]

            # if we still have left and if we still
            # didn't go there, do so
            if root.left is not None and go_left:
                stack.append([root.left, True])
            else:
                # if there is no more left, pop the last node
                # and append it to results
                results.append(stack.pop()[0].val)
                # else if there is no more left and
                # if we have something in the stack,
                # turn the go_left flag into True
                if len(stack) != 0:
                    stack[-1][-1] = False
                # if there is right from the last root, go there
                if root.right is not None:
                    stack.append([root.right, True])
        return results
