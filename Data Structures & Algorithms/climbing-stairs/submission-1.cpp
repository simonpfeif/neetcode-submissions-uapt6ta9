class Solution {
public:
    int climbStairs(int n) {
        if (n == 1) {
            return 1;
        }
        if (n == 2) {
            return 2;
        }
        int first = 1;
        int second = 1;
        for (int i = 2; i < n; i++) {
            int sum = first + second;
            first = second;
            second = sum;
        }
        return first + second;
    }
};
// 1+1=2
// 1+2=3
// 2+3=5
// 3+5=8