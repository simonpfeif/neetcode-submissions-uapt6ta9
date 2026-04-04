class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string> res;
        string curr = "";
        recursiveFunction(0, 0, n, res, curr);
        return res;
    }

private:
    void recursiveFunction(int open, int close, int n, vector<string>& res, string curr) {
        if (close > open || curr.length() > 2 * n) {
            // string is invalid
            return;
        }
        if (curr.length() == 2 * n && close == open) {
            res.push_back(curr);
        }
        else {
            recursiveFunction(open + 1, close, n, res, curr + "(");
            recursiveFunction(open, close + 1, n, res, curr + ")");
        }
        return;
    }
};
