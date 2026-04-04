class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        return dfs(nums, 0, -1);
    }

    int dfs(vector<int>& nums, int i, int curr) {
        if (i >= nums.size()) {
            return 0;
        }

        if (curr == -1 || nums[i] > nums[curr]) {
            return max(dfs(nums, i + 1, curr), 1 + dfs(nums, i + 1, i));
        }
        else {
            return dfs(nums, i + 1, curr);
        }
    }
};
