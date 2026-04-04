class Solution {
public:
    // vector<int> dailyTemperatures(vector<int>& temperatures) {
    //     vector<int> res(temperatures.size(), 0);
    //     stack<int> s;

    //     for (int i = 0; i < temperatures.size(); i++) {
    //         while (!s.empty() && temperatures[s.top()] < temperatures[i]) {
    //             res[s.top()] = i - s.top();
    //             s.pop();
    //         }
    //         s.push(i);
    //     }
    //     return res;
    // }
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        vector<int> res(temperatures.size(), 0);
        int n = temperatures.size();

        for (int i = n - 2; i >= 0; i--) {
            int j = i + 1;
            while (j < n && temperatures[j] <= temperatures[i]) {
                if (res[j] == 0) {
                    j = n;
                }
                j += res[j];
            }
            if (j < n) {
                res[i] = j - i;
            }
            
        }
        return res;
    }
};

// 30(0)
// 38(1) t[0] = 1 - 0
// 30(2) 38(1)
// 36(3) 38(1) t[2] = 3 - 2
// 35(4) 36(3) 38(1)

// 0 0 0 0 0 0 
// 
