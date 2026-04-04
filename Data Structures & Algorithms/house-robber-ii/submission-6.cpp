class Solution {
public:
    unordered_map<string, int> dp;

    int rob(vector<int>& nums) {
        if (nums.size() == 1) {
            return nums[0];
        }
        return max(dfs(nums, 0, nums.size() - 1), dfs(nums, 1, nums.size()));
    }
private:
    int dfs(vector<int>& nums, int i, int end) {
        if (i >= end) {
            return 0;
        }
        if (!dp[to_string(i) + "," + to_string(end)]) {
            dp[to_string(i) + "," + to_string(end)] = max(nums[i] + dfs(nums, i + 2, end), dfs(nums, i + 1, end));
        }
        return dp[to_string(i) + "," + to_string(end)];
        
    }

};
