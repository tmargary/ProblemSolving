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
    # Time complexity: O(n)
    # Space complexity: O(n)

    length = 0

    def rec(self, node, length):
        if node is None:
            return length

        length = max(
            self.rec(node.left, length + 1),
            self.rec(node.right, length + 1)
        )

        self.length = max(length, self.length)
        return self.length

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.rec(root, self.length)

        return self.length
