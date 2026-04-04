class Solution {
public:
    string minWindow(string s, string t) {
        if (s.length() < t.length()) return "";
        string res = "";

        unordered_map<char, int> tCount;
        unordered_map<char, int> sCount;
        for (int i = 0; i < t.length(); i++){
            tCount[t[i]]++;
        }

        int l = 0;
        int have = 0;
        int need = tCount.size();
        for (int r = 0; r < s.length(); r++) {
            sCount[s[r]]++;

            if (tCount.count(s[r]) && sCount[s[r]] == tCount[s[r]]) {
                cout << "here";
                have++;
            }

            // slide the window
            while (have == need) {
                if (r - l + 1 < res.length() || res == "") {
                    res = s.substr(l, r - l + 1);
                }

                sCount[s[l]]--;
                if (tCount.count(s[l]) && sCount[s[l]] < tCount[s[l]]) {
                    have--;
                }
                
                l++;
            }
        }
        if (have == need) {
            res = s.substr(0, s.length());
        }
        return res;
    }
};
