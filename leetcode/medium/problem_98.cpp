/*
98. Validate Binary Search Tree

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 
Example 1:
Input: root = [2,1,3]
Output: true

Example 2:
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
*/

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    bool isValidBST(TreeNode* root) {
        return isValidBSTHelper(root, nullptr, nullptr);
    }
    
    bool isValidBSTHelper(TreeNode* node, TreeNode* minNode, TreeNode* maxNode) {
        if (node == nullptr) {
            return true;
        }
        if ((minNode != nullptr && node->val <= minNode->val) ||
            (maxNode != nullptr && node->val >= maxNode->val)) {
            return false;
        }
        return isValidBSTHelper(node->left, minNode, node) &&
               isValidBSTHelper(node->right, node, maxNode);
    }
};


/*
This fails to pass some tests but it's more readable.

class Solution {
public:
    bool isValidBST(TreeNode* root) {
        return isValidBSTHelper(root);
    }
    
    bool isValidBSTHelper(TreeNode* root, int min_val = INT_MIN, int max_val = INT_MAX) {
        if (!root) {
            return true;
        }
        if (root->val <= min_val || root->val >= max_val) {
            return false;
        }
        return isValidBSTHelper(root->left, min_val, root->val) && isValidBSTHelper(root->right, root->val, max_val);
    }
};
*/