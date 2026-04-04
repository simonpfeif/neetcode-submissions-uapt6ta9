class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        priority_queue<pair<int, int>> heap;
        vector<int> res;
        int l = 0;

        for (int r = 0; r < nums.size(); r++) {
            heap.push({nums[r], r});

            if (r + 2 > k) {
                cout << r << endl;
                while (heap.top().second <= r - k) {
                    heap.pop();
                }
                res.push_back(heap.top().first);
            }
        }
        return res;
    }
};
