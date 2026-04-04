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
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        // two cases
        // 1. root is between p and q values -> ancestor will be root
        // 2. root is less than or greater than both p and q values
        while (root) {
            if (root->val < p->val && root->val < q->val) {
                root = root->right;
            }
            else if (root->val > p->val && root->val > q->val) {
                root = root->left;
            }
            else {
                return root;
            }
        }
    }
};
