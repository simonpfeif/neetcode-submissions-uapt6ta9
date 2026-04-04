class Solution {
public:
    int uniquePaths(int m, int n) {
        vector<vector<int>> grid(m+1, vector<int>(n + 1, 0));
        grid[m-1][n-1] = 1;

        for (int i = m-1; i >= 0; i--) {
            for (int j = n - 1; j >= 0; j--) {
                grid[i][j] += grid[i + 1][j] + grid[i][j+1];
            }
        }

        return grid[0][0];
    }
    // int uniquePaths(int m, int n) {
    //     return dfs(0, 0, m, n);
    // }

    // int dfs(int m_curr, int n_curr, int m, int n) {
    //     int paths = 0;
    //     if (
    //         m_curr < 0 || m_curr == m || 
    //         n_curr < 0 || n_curr == n) {
    //         return 0;
    //     }
    //     else if (n_curr == n - 1 && m_curr == m-1) {
    //         return 1;
    //     }
    //     else {
    //         return bfs(m_curr + 1, n_curr, m, n) + bfs(m_curr, n_curr + 1, m, n);
    //     }
    // }
};
