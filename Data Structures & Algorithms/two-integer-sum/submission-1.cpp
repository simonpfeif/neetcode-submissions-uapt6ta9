class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> indices;
        for (int i = 0; i < nums.size(); i++) {
            indices[nums[i]] = i;
        }
        for (int j = 0; j < nums.size(); j++) {
            int diff = target - nums[j];
            if (indices[diff] && indices[diff] != j) {
                if (j < indices[diff]){
                    return {j, indices[diff]};
                }
                else {
                    return {indices[diff], j};
                }
            }
        }
        // return {};
    }
};
