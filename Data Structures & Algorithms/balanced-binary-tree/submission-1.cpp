/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    bool isBalanced(TreeNode* root) {
        if (!root) {
            return true;
        }
        int left = getHeight(root->left);
        int right = getHeight(root->right);
        cout << "left: " << left << " right: " << right << endl;
        if (abs(left - right) > 1) {
            return false;
        }
        return isBalanced(root->left) && isBalanced(root->right);
    }

    int getHeight(TreeNode* root) {
        if (!root) {
            return 0;
        }
        return 1 + max(getHeight(root->left), getHeight(root->right));
    }
};
