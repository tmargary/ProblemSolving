"""
1379. Find a Corresponding Node of a Binary Tree in a Clone of That Tree

Given two binary trees original and cloned and given a reference to a node target in the original tree.

The cloned tree is a copy of the original tree.

Return a reference to the same node in the cloned tree.

Note that you are not allowed to change any of the two trees or the target node and the answer must be a reference to a
node in the cloned tree.

Example 1:
Input: tree = [7,4,3,null,null,6,19], target = 3
Output: 3
Explanation: In all examples the original and cloned trees are shown. The target node is a green node from the original
tree. The answer is the yellow node from the cloned tree.

Example 2:
Input: tree = [8,null,6,null,5,null,4,null,3,null,2,null,1], target = 4
Output: 4
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class SolutionItr:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:

        stack = [[original, cloned]]

        while True:
            curr = stack.pop()
            if curr[0] == target:
                return curr[1]
            if curr[0].left:
                stack.append([curr[0].left, curr[1].left])
            if curr[0].right:
                stack.append([curr[0].right, curr[1].right])


class SolutionRec:
    def getTargetCopy(self, original, cloned, target):
        if not original:
            return None

        if original == target:
            return cloned

        l = self.getTargetCopy(original.left, cloned.left, target)
        r = self.getTargetCopy(original.right, cloned.right, target)

        return l or r
