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


class Solution:

    results = list()

    def rec(self, root):
        if root:
            self.rec(root.left)
            self.results.append(root.val)
            self.rec(root.right)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.rec(root)
        return self.results
