class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> prefix(nums.size(), 1);
        vector<int> suffix(nums.size(), 1);
        int product = 1;
        for (int i = 0; i < nums.size(); i++) {
            prefix[i] = product;
            product *= nums[i];
        }

        product = 1;
        for (int i = nums.size() - 1; i >= 0; i--) {
            cout << "here" << endl;

            suffix[i] = product;
            product *= nums[i];
        }

        for (int i = 0; i < nums.size(); i++) {
            prefix[i] = prefix[i] * suffix[i];
        }
        return prefix;
    }
};
