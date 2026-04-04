class Solution {
public:
    unordered_map<int, int> cache;

    int climbStairs(int n) {
        return dfs(n, 0);
    }
    int dfs(int n, int pos){
        if (cache[pos]) {
            return cache[pos];
        }
        // base case
        if (pos == n) {
            return 1;
        }
        else if (pos > n) {
            return 0;
        }
        else {
            return cache[pos] = dfs(n, pos + 1) + dfs(n, pos + 2);
        }

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