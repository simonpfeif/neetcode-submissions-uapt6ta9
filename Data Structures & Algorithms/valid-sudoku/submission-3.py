class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = [set() for _ in range(9)]
        diags = [set() for _ in range(9)]
        for r in range(9):
            row = set()
            for c in range(9):
                cur = board[r][c]
                if cur == '.':
                    continue
                diag_pos = ((r // 3) * 3) + (c // 3)
                if cur in cols[c]:
                    return False
                elif cur in row:
                    return False
                elif cur in diags[diag_pos]:
                    return False

                row.add(cur)
                cols[c].add(cur)
                diags[diag_pos].add(cur)
        
                
        return True