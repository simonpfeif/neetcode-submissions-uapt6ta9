class Solution {
public:
    unordered_map<string, int> memo;

    int lengthOfLIS(vector<int>& nums) {
        return dfs(nums, 0, -1);
    }

    int dfs(vector<int>& nums, int i, int curr) {
        if (i >= nums.size()) {
            return 0;
        }
        if (memo.find(to_string(i) + "," + to_string(curr)) != memo.end()) {
            return memo[to_string(i) + "," + to_string(curr)];
        }
        if (curr == -1 || nums[i] > nums[curr]) {
            memo[to_string(i) + "," + to_string(curr)] =
             max(dfs(nums, i + 1, curr), 1 + dfs(nums, i + 1, i));
        }
        else {
            memo[to_string(i) + "," + to_string(curr)] = dfs(nums, i + 1, curr);
        }

        return memo[to_string(i) + "," + to_string(curr)];
    }
};
