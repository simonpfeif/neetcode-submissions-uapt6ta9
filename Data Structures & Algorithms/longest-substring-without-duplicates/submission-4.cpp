class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int res = 0;
        unordered_set<char> window;
        int l = 0;
        for (int r = 0; r < s.size(); r++) {
            while (window.find(s[r]) != window.end()) {
                window.erase(s[l]);
                l++;
            }
            window.insert(s[r]);
            res = max(res, r + 1 - l);
        }
        return res;
    }
};

// zzxyzab