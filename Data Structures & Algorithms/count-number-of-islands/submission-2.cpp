class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        // search grid
        int num = 0;
        for (int i = 0; i < grid.size(); i++) {
            for (int j = 0; j < grid[0].size(); j++) {
                if (grid[i][j] == '1') {
                    num++;
                    // dfs(grid, i, j);
                    cout << "enter bfs" << endl;
                    bfs(grid, i, j);
                }
            }
        }
        return num;
    }

    void bfs(vector<vector<char>>& grid, int i, int j) {
        queue<pair<int, int>> q;
        q.push({i, j});
        grid[i][j] = '0';

        while (!q.empty()) {
            pair<int, int> land = q.front();
            q.pop();
            cout << land.first << " " << land.second << endl;
            if (landIsIsland(grid, land.first, land.second - 1)) {
                // check up
                q.push({land.first, land.second - 1});
                grid[land.first][land.second - 1] = '0';
            }
            if (landIsIsland(grid, land.first + 1, land.second)) {
                // check right
                q.push({land.first + 1, land.second});
                grid[land.first + 1][land.second] = '0';
            }
            if (landIsIsland(grid, land.first, land.second + 1)) {
                // check down
                cout << "entered here" << endl;
                q.push({land.first, land.second + 1});
                grid[land.first][land.second + 1] = '0';
            }
            if (landIsIsland(grid, land.first - 1, land.second)){
                // check left
                q.push({land.first - 1, land.second});
                grid[land.first - 1][land.second] = '0';
            }
        }
    }

    bool landIsIsland(vector<vector<char>>& grid, int i, int j) {
        cout << "j: " << j << endl;
        if (i < 0 || j < 0 || i >= grid.size() || j >= grid[0].size() || grid[i][j] == '0') {
            return false;
        }
        else {
            return true;
        }
    }
    // void dfs(vector<vector<char>>& grid, int i, int j) {
    //     // base case is we are out of grid
    //     if (i < 0 || j < 0 || i >= grid.size() || j >= grid[0].size() || grid[i][j] == '0' || grid[i][j] == 'x') {
    //         return;
    //     }
    //     else {
    //         // mark explored land
    //         grid[i][j] = 'x';
    //     }

    //     cout << i << " " << j << endl;
    //     // check all four directions
    //     for (int d = 0; d < 4; d++) {
    //         if (d == 0) {
    //             // check up
    //             dfs(grid, i, j - 1);
    //         }
    //         else if (d == 1) {
    //             // check right
    //             dfs(grid, i + 1, j);
    //         }
    //         else if (d == 2) {
    //             // check down
    //             dfs(grid, i, j + 1);
    //         }
    //         else {
    //             // check left
    //             dfs(grid, i - 1, j);
    //         }
    //     }
    // }
    // if you find an island search through it
    // ["1","1","0","0","1"]
    // ["1","1","0","0","1"]
    // ["0","0","1","0","0"]
    // ["0","0","0","1","1"]
    
};
