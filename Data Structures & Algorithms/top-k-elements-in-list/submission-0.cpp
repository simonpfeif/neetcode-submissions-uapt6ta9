class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        vector<int> output;
        unordered_map<int, int> count;
        for (int i : nums) {
            count[i] = 1 + count[i];
        }

        vector<vector<int>> freq(nums.size() + 1);

        for (const auto& i : count){
            freq[i.second].push_back(i.first);
        }

        for (int i = freq.size() - 1; i > 0; --i) {
            for (int j : freq[i]) {
                output.push_back(j);
                if (output.size() == k){
                    return output;
                }
            }
        }


        return output;
    }
};
