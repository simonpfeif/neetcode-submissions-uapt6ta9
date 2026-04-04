class Solution {
public:
    int countSubstrings(string s) {
        int total = 0;
        unordered_map<string, bool> memo;
        for (int i = 1; i <= s.length();i++) {
            for (int j = 0; j < i; j++) {
                string substring = createSubstr(s, j, i);
                cout << j << " " << i << endl;
                cout << substring << endl; 
                if (!memo[substring]) {
                    memo[substring] = isPalidrom(substring);
                }
                total += memo[substring];
            }
        }
        return total;
    }

    string createSubstr(string original, int start, int end) {
        string out;
        while (start < end) {
            out += original[start];
            start++;
        }
        return out;
    }

    bool isPalidrom(string s) {
        string temp = s;
        reverse(s.begin(), s.end());
        cout << "temp: " << temp << " s: " << s << endl;
        bool b = temp == s;
        cout << b << endl;
        
        return temp == s;
    }
};

// jabcba

// As you check (check c)
// jabc
// abc
// bc
// c