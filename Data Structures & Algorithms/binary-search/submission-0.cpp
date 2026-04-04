class Solution {
public:
    int search(vector<int>& nums, int target) {
        int l = 0;
        int r = nums.size() - 1;

        while (l <= r) {
            int temp = (l + r) / 2;
            // cout << temp << endl;
            // cout << "left: " << l << endl;
            // cout << "right: " << r << endl;

            if (nums[temp] == target) {
                return temp;
            }
            else if (nums[temp] > target){
                r = temp - 1;
            }
            else {
                l = temp + 1;
            }
        }
        return -1;
    }
};
