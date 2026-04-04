class Solution {
public:
    // int change(int amount, vector<int>& coins) {
    //     sort(coins.begin(), coins.end());
    //     return dfs(amount, coins, 0);
    // }

    // int dfs(int amount, vector<int>& coins, int i) {
    //     if (amount == 0) {
    //         return 1;
    //     }
    //     if (i >= coins.size()) {
    //         return 0;
    //     }

    //     if (coins[i] <= amount) {
    //         return dfs(amount - coins[i], coins, i) + dfs(amount, coins, i + 1);
    //     }
    //     return 0;
    // }
    int change(int amount, vector<int>& coins) {
        sort(coins.begin(), coins.end());
        int n = coins.size();
        vector<vector<int>> mem(n + 1, vector<int>(amount + 1, 0));

        // set number of ways to get target amount = 0 to be 1
        for (int i = 0; i <= n; i++) {
            mem[i][0] = 1;
        }

        for (int i = n - 1; i >= 0; i--) {
            for (int a = 0; a <= amount; a++) {

                if (a - coins[i] >= 0) {
                    mem[i][a] = mem[i][a - coins[i]] + mem[i + 1][a];
                }
            }
        }
        return mem[0][amount];
    }
};


// x [5, 4, 3, 2, 1, 0] target amount
// 1  
// 2
// 3
// coins
// 