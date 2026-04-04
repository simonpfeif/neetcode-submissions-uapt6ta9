class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> seen;
        if (s.size() != t.size()) {
            return false;
        }
        for (int i = 0; i < s.size(); i++) {
            seen[s[i]]++;
        }
        for (int j = 0; j < t.size(); j++) {
            
            if (!seen[t[j]] || seen[t[j]] == 0) {
                return false;
            }
            else {
                seen[t[j]]--;
            }
        }
        return true;
    }
};
