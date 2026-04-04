class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        vector<int> mem(cost.size(), -1);
        return min(dfs(cost, mem, 0), dfs(cost, mem, 1));
    }
private:
    int dfs(vector<int> cost, vector<int>& mem, int i) {
        if (i >= cost.size()) {
            return 0;
        }

        if (mem[i] == -1) {
            mem[i] = cost[i] + min(dfs(cost, mem, i + 1), dfs(cost, mem, i + 2));
        }
        return mem[i];
    }
};
