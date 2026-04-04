class Solution {
public:
    int maxProfit(vector<int>& prices) {
        return dfs(prices, 0, true);
    }

    int dfs(vector<int>& prices, int day, bool buying) {
        if (day >= prices.size()) {
            return 0;
        }
        if (buying) {
            return max(dfs(prices, day + 1, false) - prices[day], dfs(prices, day + 1, buying));
        }
        else {
            // selling
            return max(prices[day] + dfs(prices, day + 2, true), dfs(prices, day + 1, buying));
            
        }
    }
};

