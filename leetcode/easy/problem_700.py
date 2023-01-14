"""
700. Search in a Binary Search Tree

You are given the root of a binary search tree (BST) and an integer val.

Find the node in the BST that the node's value equals val and return the subtree rooted with that node.
If such a node does not exist, return null.
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class MySolution1:

    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        if root.val == val:
            return root

        while root.left or root.right:
            if val < root.val:
                root = root.left
            else:
                root = root.right

            if root is None:
                return None

            if root.val == val:
                return root


class MySolution2:

    def rec_search(self, root: Optional[TreeNode], val: int):
        if root is None:
            return None
        elif root.val == val:
            return root
        else:
            if val < root.val:
                root = root.left
            else:
                root = root.right
            if root is None:
                return None
            return self.rec_search(root, val)

    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        if root.val == val:
            return root

        return self.rec_search(root, val)
