class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        vector<int> res(temperatures.size(), 0);
        stack<int> s;

        for (int i = 0; i < temperatures.size(); i++) {
            while (!s.empty() && temperatures[s.top()] < temperatures[i]) {
                res[s.top()] = i - s.top();
                s.pop();
            }
            s.push(i);
        }
        return res;
    }
};

// 30(0)
// 38(1) t[0] = 1 - 0
// 30(2) 38(1)
// 36(3) 38(1) t[2] = 3 - 2
// 35(4) 36(3) 38(1)
