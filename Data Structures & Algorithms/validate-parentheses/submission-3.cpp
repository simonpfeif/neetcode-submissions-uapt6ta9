class Solution {
public:
    bool isValid(string s) {
        stack<int> order;
        unordered_map<char, char> check;
        check['}'] = '{';
        check[']'] = '[';
        check[')'] = '(';
        
        for (int i = 0; i < s.size(); i++) {
            if (!check[s[i]]) {
                order.push(s[i]);
            }
            else if (!order.empty() && order.top() == check[s[i]]) {
                order.pop();
            }
            else {
                return false;
            }
        }
        return order.empty();
    }
};
