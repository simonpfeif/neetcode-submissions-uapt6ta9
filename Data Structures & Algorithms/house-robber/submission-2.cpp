class Solution {
public:
    vector<int> cache;

    int rob(vector<int>& nums) {
        cache.resize(nums.size(), -1);
        return max(findPath(nums, 0), findPath(nums, 1));
    }

    int findPath(vector<int>& nums, int curr) {
        cout << curr << endl;
        if (curr >= nums.size()) {
            return 0;
        }
        int maxMoney = 0;
        for (int i = curr + 2; i < nums.size(); i++) {
            if (cache[i] == -1) {
                cache[i] = findPath(nums, i);
            }
            maxMoney = max(maxMoney, cache[i]);
        }
        return nums[curr] + maxMoney;
    }
};
