class Solution {
public:
    unordered_map<int, int> dp;

    int numDecodings(string s) {
        return dfs(0, s);
    }

private:
    int dfs(int i, string& s) {
        if (i == s.length()) return 1;
        if (s[i] == '0') return 0;
        int res = 0;
        if (!dp[i + 1]) {
            dp[i + 1] = dfs(i + 1, s);
        }
        res += dp[i + 1];


        if (i + 1 < s.length() && stoi(s.substr(i,2)) < 27) {
            if (!dp[i + 2]) {
                dp[i + 2] = dfs(i + 2, s);
            }
            res += dp[i + 2];
        }
        
        return res;
    }
};
