class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        int upper = *max_element(piles.begin(), piles.end());
        int lower = 1;
        int res = upper;

        while (lower <= upper) {
            int m = (lower + upper) / 2;

            int count = 0;
            for (int i = 0; i < piles.size(); i++) {
                count += ceil(static_cast<double>(piles[i]) / m);
            }
            if (count <= h) {
                res = m;
                upper = m - 1;
            }
            else {
                lower = m + 1;
            }
        }
        return res;

    }
};