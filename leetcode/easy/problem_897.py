"""
897. Increasing Order Search Tree

Given the root of a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the
root of the tree, and every node has no left child and only one right child.

Example 1:

Input: root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]

Example 2:

Input: root = [5,1,7]
Output: [1,null,5,null,7]
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:

        stack = [[root, True]]
        results = list()

        while True:
            if len(stack) == 0:
                break
            root, go_left = stack[-1]

            if root.left is not None and go_left:
                stack.append([root.left, True])
            else:
                results.append(stack.pop()[0].val)
                if len(stack) != 0:
                    stack[-1][-1] = False
                if root.right is not None:
                    stack.append([root.right, True])

        ###################################
        new_tree = TreeNode(results.pop(0))
        tmp = new_tree
        for el in results:
            tmp.right = TreeNode(el)
            tmp = tmp.right
        return new_tree
