class Solution {
public:
    // int countSubstrings(string s) {
    //     int total = 0;
    //     unordered_map<string, bool> memo;
    //     for (int i = 1; i <= s.length();i++) {
    //         for (int j = 0; j < i; j++) {
    //             string substring = createSubstr(s, j, i);
    //             cout << j << " " << i << endl;
    //             cout << substring << endl; 
    //             if (!memo[substring]) {
    //                 memo[substring] = isPalidrom(substring);
    //             }
    //             total += memo[substring];
    //         }
    //     }
    //     return total;
    // }

    // string createSubstr(string original, int start, int end) {
    //     string out;
    //     while (start < end) {
    //         out += original[start];
    //         start++;
    //     }
    //     return out;
    // }

    // bool isPalidrom(string s) {
    //     string temp = s;
    //     reverse(s.begin(), s.end());
    //     cout << "temp: " << temp << " s: " << s << endl;
    //     bool b = temp == s;
    //     cout << b << endl;
        
    //     return temp == s;
    // }

    int countSubstrings(string s) {
        int res = 0;
        for (int i = 0; i < s.size(); i++) {
            // check odd palindrome
            res += countPalindrome(i, i, s);

            // check even palindrome
            res += countPalindrome(i, i + 1, s);
        }
        return res;
    }

    int countPalindrome(int l, int r, string s) {
        int res = 0;
        while (l >= 0 && r < s.size() && s[l] == s[r]) {
            res++;
            l--;
            r++;
        }
        return res;
    }
};

// jabcba

// As you check (check c)
// jabc
// abc
// bc
// c