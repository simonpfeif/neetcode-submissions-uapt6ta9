class Solution {
public:
    bool isPalindrome(string s) {
        
        int it1 = 0;
        int it2 = s.length() -1;

        while (it1 < it2) {
            while (it1 < it2 && !isAlphaNum(s[it1])) {
                it1++;
            }
            while (it2 > it1 && !isAlphaNum(s[it2])) {
                it2--;
            }
            cout << s[it1] << " " << s[it2] << endl;
            cout << isAlphaNum(s[it1]) << endl;
            if (tolower(s[it1]) != tolower(s[it2])) {
                cout << s[it1] << " " << s[it2] << endl;
                return false;
            }
            it1++;
            it2--;
        }
        return true;

    }

    bool isAlphaNum(char c) {
        return (c >= 'A' && c <= 'Z' || 
                c >= 'a' && c <= 'z' || 
                c >= '0' && c <= '9');
    }
};
