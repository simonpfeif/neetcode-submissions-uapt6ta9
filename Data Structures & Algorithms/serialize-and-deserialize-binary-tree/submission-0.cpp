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

class Codec {
public:

    // Encodes a tree to a single string.
    string serialize(TreeNode* root) {
        string res = "";
        dfsSerialize(root, res);
        cout << res;
        return res;
    }

    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        vector<string> vals = split(data);
        int i = 0;
        return dfsDeserialize(vals, i);
    }


private:
    void dfsSerialize(TreeNode* root, string& res) {
        if (!root) {
            res += "N,";
            cout << res << endl;
        }
        else {
            res += to_string(root->val) + ",";
            cout << res << endl;
            dfsSerialize(root->left, res);
            dfsSerialize(root->right, res);
        }
        return;
    }

    TreeNode* dfsDeserialize(vector<string> vals, int& i) {
        if (vals[i] == "N") {
            i++;
            return NULL;
        }
        else {
            TreeNode* node = new TreeNode(stoi(vals[i]));
            i++;
            node->left = dfsDeserialize(vals, i);
            node->right = dfsDeserialize(vals, i);
            return node;
        }
    }

    vector<string> split(string data) {
        vector<string> elems;
        stringstream ss(data);
        string item;
        while (getline(ss, item, ',')) {
            elems.push_back(item);
        }
        return elems;
    } 
};
