class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        // sort(nums.begin(), nums.end());
        // int last = 0;

        // for (int i = 1; i < nums.size(); ++i) {
        //     if (nums[i] == nums[last]) {
        //         return true;
        //     }
        //     last++;
        // }
        // return false;
        unordered_map<int, int> seen;

        for (int i = 0; i < nums.size(); ++i) {
            if (seen.find(nums[i]) != seen.end()) {
                return true;
            }
            seen[nums[i]] = 0;
        }
        return false;
    }
};
