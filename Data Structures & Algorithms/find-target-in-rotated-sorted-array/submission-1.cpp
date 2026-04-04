class Solution {
public:
    int search(vector<int>& nums, int target) {
        int l = 0;
        int r = nums.size() - 1;
        int rotation = 0;

        // find deflection point;
        while (l < r) {
            int temp = (r + l) / 2;
            if (nums[temp] > nums[r]) {
                l = temp + 1;
            }
            else {
                r = temp;
            }
        }
        rotation = l;
        l = 0;
        r = nums.size() - 1;

        if (target >= nums[rotation] && target <= nums[r]){
            l = rotation;
        }
        else {
            r = rotation;
        }

        while (l <= r) {
            int temp = (l + r) / 2;
            if (nums[temp] == target) {
                return temp;
            }
            if (nums[temp] < target) {
                l = temp + 1;
            }
            else {
                r = temp - 1;
            }
        }

        return -1;
    }
};
