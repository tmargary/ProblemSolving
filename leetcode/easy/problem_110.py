"""
110. Balanced Binary Tree

Given a binary tree, determine if it is
height-balanced.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: true
Example 2:
Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
Example 3:
Input: root = []
Output: true
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def getHeight(self, node):
        if not node:
            return 0

        return 1 + max(self.getHeight(node.left), self.getHeight(node.right))

    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        if root==None:
            return True

        check_1 = abs(self.getHeight(root.left) - self.getHeight(root.right)) <= 1
        check_2 = self.isBalanced(root.left)
        check_3 = self.isBalanced(root.right)

        return check_1 and check_2 and check_3
