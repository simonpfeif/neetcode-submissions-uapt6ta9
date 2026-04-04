class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res =[]
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        while left < right and top < bottom:
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1

            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right -= 1

            if not (left < right and top < bottom):
                break

            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1

            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
        return res

        # res = []
        # row = col = 0
        # directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        # d = 0

        # while matrix[row][col] >= -100:
        #     res.append(matrix[row][col])
        #     matrix[row][col] = -101
            
        #     r = row + directions[d][0]
        #     c = col + directions[d][1]

        #     if r >= len(matrix) or r < 0 or c >= len(matrix[0]) or c < 0 or matrix[r][c] == -101:
        #         d = d + 1 if d < 3 else 0
        #         r = row + directions[d][0]
        #         c = col + directions[d][1]
        #         if r >= len(matrix) or r < 0 or c >= len(matrix[0]) or c < 0 or matrix[r][c] == -101:
        #             return res

        #     row = r
        #     col = c
        
        # return res