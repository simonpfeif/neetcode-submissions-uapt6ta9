class Solution {
public:
    bool canPartition(vector<int>& nums) {
        // nums must sum to an even number
        int sum = 0;
        for (int i = 0; i < nums.size(); i++) {
            sum += nums[i];
        }
        if (sum % 2 == 1) {
            return false;
        }

        // find some combination of array to equal sum/2
        return dfs(nums, sum/2, 0);
    }

    bool dfs(vector<int>& nums, int target, int i) {
        if (target == 0) {
            return true;
        }
        else if (i >= nums.size() || target < 0) {
            return false;
        }

        return dfs(nums, target - nums[i], i + 1) || dfs(nums, target, i + 1);
    }
};
