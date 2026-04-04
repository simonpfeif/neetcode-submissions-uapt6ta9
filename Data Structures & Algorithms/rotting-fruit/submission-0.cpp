class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {

        queue<pair<int, int>> q;
        int fresh = 0;
        int time = 0;
        // initial iteration to find all rotten fruit
        for (int i = 0; i < grid.size(); i++) {
            for (int j = 0; j < grid[i].size(); j++) {
                if (grid[i][j] == 2) {
                    q.push({i, j});
                }
                if (grid[i][j] == 1) {
                    fresh++;
                }
            }
        }

        vector<vector<int>> dirs = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};

        // do multi BFS
        while (fresh > 0 && !q.empty()) {
            int curr_size = q.size();

            for (int i = 0; i < curr_size; i++) {
                int row = q.front().first;
                int col = q.front().second;
                q.pop();

                for (int d = 0; d < 4; d++) {
                    int r = row + dirs[d][0];
                    int c = col + dirs[d][1];

                    if (r < grid.size() && r >= 0 && c < grid[0].size() && c >= 0 && grid[r][c] == 1) {
                        q.push({r,c});
                        fresh--;
                        grid[r][c] = 2;
                        cout << " pushing: " << r << " " << c << endl;
                        cout << "fresh: " << fresh << endl;
                    }
                }
            }

            time++;
        }
        if (fresh == 0) {
            return time;
        }
        else {
            return -1;
        }
    }
};
