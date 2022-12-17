"""
104. Maximum Depth of Binary Tree

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the
farthest leaf node.
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    max_depth = 0

    def rec(self, node, length):
        if not node:
            return 0
        if not node.left and not node.right:
            self.max_depth = max(self.max_depth, length)

        self.rec(node.left, self.max_depth + 1)
        self.rec(node.right, self.max_depth + 1)

    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        self.rec(root, self.max_depth)

        return self.max_depth + 1
