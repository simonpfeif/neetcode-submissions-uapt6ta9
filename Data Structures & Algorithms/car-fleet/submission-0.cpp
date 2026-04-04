class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        int res = 1;
        int n = position.size();

        vector<pair<int, int>> cars;
        for (int i = 0; i < n; i++) {
            cars.push_back({position[i], speed[i]});
        }
        sort(cars.rbegin(), cars.rend());

        double fleet = (double)(target - cars[0].first) / cars[0].second;
        cout << fleet << endl;
        for (int i = 1; i < n; i++) {
            double time = (double)(target - cars[i].first) / cars[i].second;
            cout << time << endl;
            if (fleet < time) {
                res++;
                fleet = time;
            }
        }

        return res;
    }
};
