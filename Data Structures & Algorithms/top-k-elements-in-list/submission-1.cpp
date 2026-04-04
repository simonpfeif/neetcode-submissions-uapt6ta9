class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        // vector<int> output;
        // unordered_map<int, int> count;
        // for (int i : nums) {
        //     count[i] = 1 + count[i];
        // }

        // vector<vector<int>> freq(nums.size() + 1);

        // for (const auto& i : count){
        //     freq[i.second].push_back(i.first);
        // }

        // for (int i = freq.size() - 1; i > 0; --i) {
        //     for (int j : freq[i]) {
        //         output.push_back(j);
        //         if (output.size() == k){
        //             return output;
        //         }
        //     }
        // }


        // return output;













        unordered_map<int, int> count;
        for (int num : nums){
            count[num] = 1 + count[num];
        }

        vector<pair<int, int>> hash_flip;
        for (auto& i : count) {
            hash_flip.push_back({i.second, i.first});
        }
        // sort in reverse order
        sort(hash_flip.rbegin(), hash_flip.rend());

        vector<int> out;

        for (int i = 0; i < k; i++) {
            out.push_back(hash_flip[i].second);
        }
        return out;


        
    }
};
