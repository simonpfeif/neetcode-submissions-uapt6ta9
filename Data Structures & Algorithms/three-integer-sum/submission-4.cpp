class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> res;
        if (nums.size() == 0) return res;

        sort(nums.begin(), nums.end());
        
        for (int i = 0; i < nums.size(); i++) {
            if (i > 0 && nums[i - 1] == nums[i]) continue;
            int l = i + 1;
            int r = nums.size() - 1;

            while(l < r) {
                if ((nums[i] + nums[l] + nums[r]) == 0) {
                    vector<int> temp(3);
                    temp[0] = nums[i];
                    temp[1] = nums[l];
                    temp[2] = nums[r];
                    res.push_back(temp);
                    l++;
                    r--;
                    while (l < r && nums[r] == nums[r+1]) {
                        r--;
                    }
                }
                else if ((nums[i] + nums[l] + nums[r]) > 0) {
                    r--;
                }
                else {
                    l++;
                }
            }

        }
        
        return res;
    }
};
