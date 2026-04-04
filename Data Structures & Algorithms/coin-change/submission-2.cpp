class Solution {
public:
    unordered_map<int, int> dp;
    int coinChange(vector<int>& coins, int amount) {
        int min = dfs(coins, amount);
        if (min == 1e9) {
            return -1;
        }
        else {
            return min;
        }
    }

private:
    int dfs(vector<int>& coins, int subAmount) {
        if (subAmount == 0) {
            return 0;
        }
        int res = 1e9;
        for (int i = 0; i < coins.size(); i++) {
            if (subAmount - coins[i] >= 0) {
                if (!dp[subAmount - coins[i]]) {
                    dp[subAmount - coins[i]] = dfs(coins, subAmount - coins[i]);
                }
                res = min(res, 1 + dp[subAmount - coins[i]]);
            }
        }
        return res;
    }
};
