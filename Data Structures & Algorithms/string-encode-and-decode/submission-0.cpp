class Solution {
public:

    string encode(vector<string>& strs) {
        string res = "";
        for (int i = 0; i < strs.size(); i++) {
            res += strs[i] + "|";
        }
        return res;
    }

    vector<string> decode(string s) {
        string tmp; 
        stringstream ss(s);
        vector<string> words;

        while(getline(ss, tmp, '|')){
            words.push_back(tmp);
        }
        return words;
    }
};
