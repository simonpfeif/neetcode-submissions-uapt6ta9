class Solution {
public:
    int directions[4][2] = {{0,1}, {1,0}, {-1,0},{0,-1}};
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int biggestIsland = 0;
        for (int i = 0; i < grid.size(); i++) {
            for (int j = 0; j < grid[0].size(); j++) {
                if (grid[i][j] == 1) {
                    biggestIsland = max(dfs(grid, i, j), biggestIsland);
                }
            }
        }
        return biggestIsland;
    }
    int dfs(vector<vector<int>>& grid, int i, int j) {
        int islandTotal = 0;
        cout << i << " " << j << endl;
        // base case
        if (i < 0 || j < 0 || i >= grid.size() || j >= grid[0].size() || grid[i][j] == 0) {
            return islandTotal;
        }
        else {
            islandTotal++;
            grid[i][j] = 0;
        }
        
        // recursive step
        for (int d = 0; d < 4; d++) {
            islandTotal += dfs(grid, i + directions[d][0], j + directions[d][1]);
        }
        return islandTotal;
    }
};
