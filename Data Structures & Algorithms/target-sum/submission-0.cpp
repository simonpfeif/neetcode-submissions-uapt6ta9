class Solution {
public:
    unordered_map<string, int> dp;

    int findTargetSumWays(vector<int>& nums, int target) {
        return dfs(nums, 0, 0, target);
    }
    int dfs(vector<int>& nums, int i, int sum, int target) {
        if (i == nums.size()) {
            if (target == sum) {
                return 1;
            }
            else {
                return 0;
            }
        }
        if (dp[to_string(i) + "-" + to_string(sum)]) {
            return dp[to_string(i) + "-" + to_string(sum)];
        }
        else {
            dp[to_string(i) + "-" + to_string(sum)] = 
            dfs(nums, i + 1, sum + nums[i], target) + 
            dfs(nums, i + 1, sum - nums[i], target);
        }
        return dp[to_string(i) + "-" + to_string(sum)];
    }
};


// target = 2
// [ 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6]
// 2 
// 2 
// 2