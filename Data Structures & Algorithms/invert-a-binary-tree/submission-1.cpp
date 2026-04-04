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
    // bfs
    TreeNode* invertTree(TreeNode* root) {
        if (!root) {
            return nullptr;
        }
        queue<TreeNode*> dfs;
        dfs.push(root);

        while(!dfs.empty()) {
            TreeNode* node = dfs.front();
            swap(node->left, node->right);

            if (node->left) {
                dfs.push(node->left);
            }
            if (node->right) {
                dfs.push(node->right);
            }
            dfs.pop();
        }
        return root;
    }

    // dfs
    // TreeNode* invertTree(TreeNode* root) {
    //     if (root == nullptr) {
    //         return nullptr;
    //     }
    //     TreeNode* node = new TreeNode(root->val);

    //     node->right = invertTree(root->left);
    //     node->left = invertTree(root->right);

    //     return node;
    // }
};
