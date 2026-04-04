class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> output;
        sort(nums.begin(), nums.end());
        for (int i = 0; i < nums.size(); i++) {
            int j = i + 1;
            int k = nums.size() - 1;
            int target = -nums[i];

            if (nums[i] > 0) break;
            if (i > 0 && nums[i] == nums[i - 1]) continue;
            // cout << nums[i] << " " << nums[j] << " " << nums[k] << endl;
            while (j < k) {
                cout << nums[i] << " " << nums[j] << " " << nums[k] << endl;
                if (nums[j] + nums[k] < target) {
                    j++;
                }
                else if (nums[j] + nums[k] > target) {
                    k--;
                }
                else if (nums[j] + nums[k] == target) {
                    // vector<int> temp;
                    // temp.push_back(nums[i]);
                    // temp.push_back(nums[j]);
                    // temp.push_back(nums[k]);
                    output.push_back({nums[i], nums[j], nums[k]});
                    j++;
                    k--;
                    while (j < k && nums[j] == nums[j - 1]) {
                        j++;
                    }
                }
                else {
                    j++;
                    k--;
                }
            }
        }
        return output;
    }
};
