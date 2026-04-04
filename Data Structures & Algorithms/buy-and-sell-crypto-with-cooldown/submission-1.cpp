class Solution {
public:
    unordered_map<string, int> memo;
    int maxProfit(vector<int>& prices) {
        return dfs(prices, 0, true);
    }

    int dfs(vector<int>& prices, int day, bool buying) {
        if (day >= prices.size()) {
            return 0;
        }
        string key = to_string(day) + "-" + to_string(buying);
        if (memo[key]){
            return memo[key];
        }

        if (buying) {
            memo[key] = max(dfs(prices, day + 1, false) - prices[day], dfs(prices, day + 1, buying));
        }
        else {
            // selling
            memo[key] = max(prices[day] + dfs(prices, day + 2, true), dfs(prices, day + 1, buying));
        }
        return memo[key];
    }
};

