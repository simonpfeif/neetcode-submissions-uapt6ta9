class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        sort(piles.begin(), piles.end());
    
        int biggest_pile = piles[piles.size() - 1];
        for (int k = 1; k < biggest_pile; k++) {
            long long time = 0;
            for (int i = 0; i < piles.size(); i++) {
                time += (piles[i] + k - 1) / k;
            }
            if (time <= h) {
                return k;
            }
        }

    }
};

// k = bananas/hr eating rate
// upper bound k = max pile * num piles / h