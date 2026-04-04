class Solution {
public:
    void islandsAndTreasure(vector<vector<int>>& grid) {
        vector<vector<int>> dirs = {{0, 1}, {1, 0}, {-1, 0}, {0, -1}};
        queue<pair<int, int>> q;
        int n = grid.size();
        int m = grid[0].size();

        // Find chests
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (grid[i][j] == 0) {
                    q.push({i, j});
                }
            }
        }

        while (!q.empty()) {
            int row = q.front().first;
            int col = q.front().second;
            q.pop();

            for (int i = 0; i < 4; i++) {
                int r = row + dirs[i][0];
                int c = col + dirs[i][1];
                
                if (r >= n || r < 0 || c >= m || c < 0 || 
                    grid[r][c] != 2147483647) {
                    continue;
                }
                q.push({r, c});
                grid[r][c] = grid[row][col] + 1;
            }
        }
    }
};
