class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int curr_max = 0;
        unordered_set<char> curr;
        int l = 0;

        for (int r = 0; r < s.size(); r++) {
            while(curr.find(s[r]) != curr.end()) {
                curr.erase(s[l]);
                l++;
            }
            curr.insert(s[r]);
            curr_max = max(curr_max, r-l+1);
        }
        return curr_max;
    }
};

// zzxyzab