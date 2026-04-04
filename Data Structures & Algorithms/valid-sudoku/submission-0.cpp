class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        unordered_map<int, unordered_set<int>> rows, cols;
        unordered_map<string, unordered_set<int>> squares;

        for (int r = 0; r < board.size(); r++) {
            for (int c = 0; c < board[r].size(); c++) {
                if (board[r][c] == '.') continue;

                int row = r / 3;
                int col = c / 3;
                string square_key = to_string(row) + "," + to_string(col);

                if (rows[r].count(board[r][c]) 
                || cols[c].count(board[r][c]) 
                || squares[square_key].count(board[r][c])) {
                    return false;
                }

                rows[r].insert(board[r][c]);
                cols[c].insert(board[r][c]);
                squares[square_key].insert(board[r][c]);
            }
        }
        return true;
    }
};
