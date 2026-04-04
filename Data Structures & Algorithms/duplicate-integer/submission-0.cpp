class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int last = 0;

        for (int i = 1; i < nums.size(); ++i) {
            if (nums[i] == nums[last]) {
                return true;
            }
            last++;
        }
        return false;
    }
};
