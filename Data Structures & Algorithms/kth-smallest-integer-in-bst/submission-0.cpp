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
    int kthSmallest(TreeNode* root, int k) {
        vector<int> res(2);
        res[0] = k;
        dfs(root, res);
        return res[1];
    }

private:
    void dfs(TreeNode* root, vector<int>& res) {
        if (!root) {
            res[0]--;
            return;
        }
        dfs(root->left, res);
        if (res[0] == 0) {
            res[1] = root->val;
        }
        dfs(root->right, res);
    }
};
