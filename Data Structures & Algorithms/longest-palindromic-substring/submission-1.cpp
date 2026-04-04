class Solution {
public:
    string longestPalindrome(string s) {
        int resIdx = 0, resLen = 0;
        for (int i = 0; i < s.length(); i++) {
            int l = i;
            int r = i;
            while (l >= 0 && r < s.length() && s[l] == s[r]) {
                if (r - l + 1 > resLen) {
                    resIdx = l;
                    resLen = r - l + 1;
                }
                l--;
                r++;
            }
    
            l = i - 1;
            r = i;
            while (l >= 0 && r < s.length() && s[l] == s[r]) {
                if (r - l + 1 > resLen) {
                    resIdx = l;
                    resLen = r - l + 1;
                }
                l--;
                r++;
            }
        }
        return s.substr(resIdx, resLen);
    }

};
