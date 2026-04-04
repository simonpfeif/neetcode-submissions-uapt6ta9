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
    int goodNodes(TreeNode* root) {
        if (root) {
            return dfs(root, root->val);
        }
        else {
            return 0;
        }
    }
private:
    int dfs(TreeNode* root, int x) {
        if (!root) {
            return 0;
        }
        else if (root->val < x) {
            return dfs(root->left, x) + dfs(root->right, x);
        }
        else {
            // root->val > x
            return 1 + dfs(root->left, root->val) + dfs(root->right, root->val);
        }
    }
};
