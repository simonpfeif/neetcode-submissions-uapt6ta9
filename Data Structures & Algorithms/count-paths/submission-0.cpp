class Solution {
public:
    int uniquePaths(int m, int n) {
        return bfs(0, 0, m, n);
    }

    int bfs(int m_curr, int n_curr, int m, int n) {
        int paths = 0;
        if (
            m_curr < 0 || m_curr == m || 
            n_curr < 0 || n_curr == n) {
            return 0;
        }
        else if (n_curr == n - 1 && m_curr == m-1) {
            return 1;
        }
        else {
            return bfs(m_curr + 1, n_curr, m, n) + bfs(m_curr, n_curr + 1, m, n);
        }
    }
};
