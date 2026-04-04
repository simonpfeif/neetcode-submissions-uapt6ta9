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
    bool isValidBST(TreeNode* root) {
        return dfs(root, -INFINITY, INFINITY);
    }
private:
    bool dfs(TreeNode* root, int lower, int upper) {
        if (!root) {
            return true;
        }

        if (!(lower < root->val && root->val < upper)) {
            return false;
        }
        
        return dfs(root->left, lower, root->val) && dfs(root->right, root->val, upper);
    }
};

// dfs(6, lower= 5, upper= inf)