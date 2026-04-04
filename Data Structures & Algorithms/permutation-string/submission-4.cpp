class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        if (s1.length() > s2.length()) {
            return false;
        }

        vector<int> s1Count(26, 0);
        vector<int> s2Count(26, 0);
        for (int i = 0; i < s1.length(); i++) {
            s1Count[s1[i] - 'a']++;
            s2Count[s2[i] - 'a']++;
        }

        int matches = 0;
        for (int i = 0; i < 26; i++) {
            if (s1Count[i] == s2Count[i]) {
                matches++;
            }
        }

        int l = 0;
        for (int r = s1.length(); r < s2.length(); r++) {
            if (matches == 26) {
                return true;
            }
            s2Count[s2[l] - 'a']--;
            if (s1Count[s2[l] -'a'] == s2Count[s2[l] - 'a']) {
                matches++;
            }
            else if (s1Count[s2[l] -'a'] - 1 == s2Count[s2[l] - 'a']) {
                matches--;
            }
            l++;

            s2Count[s2[r] - 'a']++;
            if (s1Count[s2[r] - 'a'] == s2Count[s2[r] - 'a']) {
                matches++;
            }
            else if (s1Count[s2[r] - 'a'] + 1 == s2Count[s2[r] - 'a']) {
                matches--;
            }
        }
        return matches == 26;
    }
};
