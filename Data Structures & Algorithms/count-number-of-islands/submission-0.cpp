class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        // search grid
        int num = 0;
        for (int i = 0; i < grid.size(); i++) {
            for (int j = 0; j < grid[0].size(); j++) {
                if (grid[i][j] == '1') {
                    num++;
                    dfs(grid, i, j);
                }
            }
        }
        return num;
    }
    void dfs(vector<vector<char>>& grid, int i, int j) {
        // base case is we are out of grid
        if (i < 0 || j < 0 || i >= grid.size() || j >= grid[0].size() || grid[i][j] == '0') {
            return;
        }
        else {
            // mark explored land
            grid[i][j] = '0';
        }

        cout << i << " " << j << endl;
        // check all four directions
        for (int d = 0; d < 4; d++) {
            if (d == 0) {
                // check up
                dfs(grid, i, j - 1);
            }
            else if (d == 1) {
                // check right
                dfs(grid, i + 1, j);
            }
            else if (d == 2) {
                // check down
                dfs(grid, i, j + 1);
            }
            else {
                // check left
                dfs(grid, i - 1, j);
            }
        }
    }
    // if you find an island search through it
    // ["1","1","0","0","1"]
    // ["1","1","0","0","1"]
    // ["0","0","1","0","0"]
    // ["0","0","0","1","1"]
    
};
