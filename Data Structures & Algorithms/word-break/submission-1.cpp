class Solution {
public:
    unordered_map<int, bool> memo;

    bool wordBreak(string s, vector<string>& wordDict) {
        memo[s.length()] = true;
        return dfs(s, wordDict, 0);
    }

    bool dfs(string& s, vector<string> &wordDict, int i) {
        if (memo.find(i) != memo.end()) {
            return memo[i];
        }

        for (const string& word : wordDict) {
            if (word.length() + i <= s.length() && s.substr(i, word.length()) == word) {
                if (dfs(s, wordDict, i + word.length())) {
                    memo[i] = true;
                    return true;
                }
            }
        }
        
        memo[i] = false;
        return false;
    }
};
