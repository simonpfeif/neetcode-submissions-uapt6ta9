class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> s;
        for (int i = 0; i < tokens.size(); i++) {
            if (tokens[i][0] == '+') {
                int temp = s.top();
                s.pop();
                temp = s.top() + temp;
                s.pop();
                s.push(temp);
            }
            else if (tokens[i][0] == '/') {
                int temp = s.top();
                s.pop();
                cout << "top: " << s.top() << " temp: " << temp << endl;
                temp = s.top() / temp;
                s.pop();
                cout << temp << endl;
                s.push(temp);
            }
            else if (tokens[i] == "-") {
                int temp = s.top();
                s.pop();
                temp = s.top() - temp;
                s.pop();
                s.push(temp);
            }
            else if (tokens[i][0] == '*') {
                int temp = s.top();
                s.pop();
                temp = s.top() * temp;
                s.pop();
                s.push(temp);
            }
            else {
                cout << "push: " << stoi(tokens[i]) << endl;
                s.push(stoi(tokens[i]));
            }
        }
        return s.top();
    }
};
