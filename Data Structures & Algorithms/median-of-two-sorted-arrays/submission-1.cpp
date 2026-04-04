class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int target = (nums1.size() + nums2.size() + 1) / 2;
        bool odd = (nums1.size() + nums2.size()) % 2;
        vector<int> big;
        vector<int> small;
        if (nums1.size() < nums2.size()) {
            big = nums2;
            small = nums1;
        }
        else {
            big = nums1;
            small = nums2;
        }

        // run binary search on small
        int l = 0;
        int r = small.size();
        while (l <= r) {
            int smallMid = (r + l) / 2;
            int bigMid = target - smallMid;

            int smallLeft = smallMid > 0 ? small[smallMid - 1] : INT_MIN;
            int smallRight = smallMid < small.size() ? small[smallMid] : INT_MAX;
            int bigLeft = bigMid > 0 ? big[bigMid - 1] : INT_MIN;
            int bigRight = bigMid < big.size() ? big[bigMid] : INT_MAX;

            cout << "smallLeft: " << smallLeft << endl;
            cout << "bigRight: " << bigRight << endl;
            cout << "smallRight: " << smallRight << endl;
            cout << "bigLeft: " << bigLeft << endl;
            if (smallLeft <= bigRight && bigLeft <= smallRight) {
                if (odd) {
                    return max(smallLeft, bigLeft);
                }
                else {
                    return (max(smallLeft, bigLeft) + min(smallRight, bigRight)) / 2.0;
                }
            }
            else if (smallLeft > bigRight) {
                r = smallMid - 1;
            }
            else {
                l = smallMid + 1;
            }
        }

        return -1;
    }
};

