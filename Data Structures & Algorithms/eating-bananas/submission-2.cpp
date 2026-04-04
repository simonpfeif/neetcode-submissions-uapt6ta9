class Solution {
public:
    // int minEatingSpeed(vector<int>& piles, int h) {
    //     sort(piles.begin(), piles.end());
    
    //     int biggest_pile = piles[piles.size() - 1];
    //     for (int k = 1; k < biggest_pile; k++) {
    //         long long time = 0;
    //         for (int i = 0; i < piles.size(); i++) {
    //             time += (piles[i] + k - 1) / k;
    //         }
    //         if (time <= h) {
    //             return k;
    //         }
    //     }

    // }
    int minEatingSpeed(vector<int>& piles, int h) {
        int l = 1;
        int r = *max_element(piles.begin(), piles.end());
        int res = r;
        while(l <= r) {
            int k = (l + r)/ 2;
            long long time = 0;
            for (int i = 0; i < piles.size(); i++) {
                time += ceil(static_cast<double>(piles[i]) / k);
            }
            if (time <= h) {
                res = k;
                r = k - 1;
            }
            else {
                l = k + 1;
            }
        }
        return res;
    }
};

// k = bananas/hr eating rate
// upper bound k = max pile * num piles / h