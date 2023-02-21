/*
226. Invert Binary Tree

Given the root of a binary tree, invert the tree, and return its root.

Example 1:

Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Example 2:

Input: root = [2,1,3]
Output: [2,3,1]

Example 3:

Input: root = []
Output: []
*/

// Definition for a binary tree node.
struct TreeNode
{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution
{
public:
    void invertHelper(TreeNode *root)
    {
        if (root == nullptr)
        {
            return;
        }

        TreeNode *tmp = root->right;
        root->right = root->left;
        root->left = tmp;

        invertHelper(root->left);
        invertHelper(root->right);
    }

    TreeNode *invertTree(TreeNode *root)
    {
        invertHelper(root);
        return root;
    }
};