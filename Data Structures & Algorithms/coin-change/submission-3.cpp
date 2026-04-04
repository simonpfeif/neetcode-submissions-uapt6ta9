class Solution {
// Bottom up:
public:
    int coinChange(vector<int>& coins, int amount) {
        vector<int> dp(amount + 1, amount + 1);
        dp[0] = 0;
        for (int i = 1; i <= amount; i++) {
            for (int j = 0; j < coins.size(); j++) {
                if (coins[j] <= i) {
                    dp[i] = min(dp[i], 1 + dp[i - coins[j]]);
                }
            }
        }
        if (dp[amount] == amount + 1) {
            return -1;
        }
        else {
            return dp[amount];
        }
        
    }


// Top down:
// public:
//     unordered_map<int, int> dp;
//     int coinChange(vector<int>& coins, int amount) {
//         int min = dfs(coins, amount);
//         if (min == 1e9) {
//             return -1;
//         }
//         else {
//             return min;
//         }
//     }

// private:
//     int dfs(vector<int>& coins, int subAmount) {
//         if (subAmount == 0) {
//             return 0;
//         }
//         int res = 1e9;
//         for (int i = 0; i < coins.size(); i++) {
//             if (subAmount - coins[i] >= 0) {
//                 if (!dp[subAmount - coins[i]]) {
//                     dp[subAmount - coins[i]] = dfs(coins, subAmount - coins[i]);
//                 }
//                 res = min(res, 1 + dp[subAmount - coins[i]]);
//             }
//         }
//         return res;
//     }
};
