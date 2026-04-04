class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> hashmap;
        // arr of 26 letters as the key, list of words as the value

        for (int i = 0; i < strs.size(); i++) {
            vector<int> count(26, 0);

            for (int j = 0; j < strs[i].size(); j++) {
                count[strs[i][j] - 'a']++;
            }

            string key = to_string(count[0]);
            for (int k = 1; k < 26; k++) {
                key += ", " + to_string(count[k]);
            }
            hashmap[key].push_back(strs[i]);
        }

        vector<vector<string>> res;
        for (const auto& pair : hashmap) {
            res.push_back(pair.second);
        }
        return res;
    }
};
