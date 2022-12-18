"""
938. Range Sum of BST

Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a
value in the inclusive range [low, high].

Example 1:

Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
Output: 32
Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.

Example 2:

Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
Output: 23
Explanation: Nodes 6, 7, and 10 are in the range [6, 10]. 6 + 7 + 10 = 23.

"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class SolutionItr:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        stack = [root]

        sum_ = 0
        while True:

            if not len(stack):
                return sum_

            curr = stack.pop()

            if curr.val >= low and curr.val <= high:
                sum_ += curr.val

            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)


class SolutionRec:

    sum_ = 0

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        if not root:
            return 0

        if low <= root.val <= high:
            l = self.rangeSumBST(root.left, low, high)
            r = self.rangeSumBST(root.right, low, high)
            return root.val + l + r
        elif root.val < low:
            return self.rangeSumBST(root.right, low, high)
        else:
            return self.rangeSumBST(root.left, low, high)
