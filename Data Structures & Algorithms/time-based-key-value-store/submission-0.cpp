class TimeMap {
private:
    unordered_map<string, vector<pair<int, string>>> timeMap;
public:
    TimeMap() {}
    
    void set(string key, string value, int timestamp) {
        timeMap[key].emplace_back(timestamp, value);
    }
    
    string get(string key, int timestamp) {
        int l = 0;
        int r = timeMap[key].size() - 1;
        string res = "";
        while (l <= r) {
            int mid = (l + r) / 2;
            if (timeMap[key][mid].first > timestamp) {
                r = mid - 1;
            }
            else {
                res = timeMap[key][mid].second;
                l = mid + 1;
            }
        }
        return res;
    }
};
