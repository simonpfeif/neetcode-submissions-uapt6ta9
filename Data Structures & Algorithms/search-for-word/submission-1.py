class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        ROWS = len(board)
        COLS = len(board[0])
        
        def dfs(r, c, i):
            if i == len(word):
                return True
            
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or board[r][c] != word[i] or board[r][c] == '.':
                return False
            
            letter = board[r][c]
            board[r][c] = "." # mark board for edge case like banana
            for d in directions:
                if dfs(r + d[0], c + d[1], i + 1):
                    return True

            board[r][c] = letter # backtrack
            return False


        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False
