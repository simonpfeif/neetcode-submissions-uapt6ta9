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
    bool isSameTree(TreeNode* p, TreeNode* q) {
        queue<TreeNode*> p_bfs;
        queue<TreeNode*> q_bfs;
        p_bfs.push(p);
        q_bfs.push(q);
        while(!p_bfs.empty() && !q_bfs.empty()) {
            TreeNode* node_p = p_bfs.front();
            TreeNode* node_q = q_bfs.front();
            p_bfs.pop();
            q_bfs.pop();
            if (!node_p && !node_q) {
                continue;
            }
            else if (!node_p || 
                !node_q || 
                node_p->val != node_q->val) {
                return false;
            }
            
            p_bfs.push(node_p->left);
            p_bfs.push(node_p->right);
            q_bfs.push(node_q->left);
            q_bfs.push(node_q->right);
        }
        return true;
    }
};
