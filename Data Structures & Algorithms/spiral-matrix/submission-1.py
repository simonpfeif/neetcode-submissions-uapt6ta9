class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        row = col = 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        d = 0

        while matrix[row][col] >= -100:
            res.append(matrix[row][col])
            matrix[row][col] = -101
            
            r = row + directions[d][0]
            c = col + directions[d][1]

            if r >= len(matrix) or r < 0 or c >= len(matrix[0]) or c < 0 or matrix[r][c] == -101:
                d = d + 1 if d < 3 else 0
                r = row + directions[d][0]
                c = col + directions[d][1]
                if r >= len(matrix) or r < 0 or c >= len(matrix[0]) or c < 0 or matrix[r][c] == -101:
                    return res

            row = r
            col = c
        
        return res