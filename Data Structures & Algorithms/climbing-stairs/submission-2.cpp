class Solution {
public:
    int climbStairs(int n) {
        return dfs(n, 0);
    }
    int dfs(int n, int pos){
        int numClimbs = 0;

        // base case
        if (pos == n) {
            numClimbs++;
        }
        else if (pos > n) {
            return 0;
        }
        else {
            numClimbs += dfs(n, pos + 1);
            numClimbs += dfs(n, pos + 2);
        }
        return numClimbs;

    }
};
// 1+1=2
// 1+2=3
// 2+3=5
// 3+5=8


// public:
//     int climbStairs(int n) {
//         if (n == 1) {
//             return 1;
//         }
//         if (n == 2) {
//             return 2;
//         }
//         int first = 1;
//         int second = 1;
//         for (int i = 2; i < n; i++) {
//             int sum = first + second;
//             first = second;
//             second = sum;
//         }
//         return first + second;
//     }
// };