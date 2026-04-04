class Solution {
public:
    int longestConsecutive(vector<int>& nums) {

        unordered_set<int> hash(nums.begin(), nums.end());
        if (nums.size() == 0) return 0;
        int res = 1;

        for (int i = 0; i < nums.size(); i++) {
            if (hash.find(nums[i] - 1) != hash.end()) {
                int length = 2;
                while (hash.find(nums[i] - length) != hash.end()) {
                    length++;
                }
                res = max(res, length);
            }
        }

        return res;
    }
};
