class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bottom = 0, len(matrix) - 1

        row = 0
        while top <= bottom:

            m = (top + bottom) // 2

            if matrix[m][0] <= target:
                row = m
                top = m + 1
            else:
                bottom = m - 1
        
        l, r = 0, len(matrix[row]) - 1
        while l <= r:
            m = (l + r) // 2

            if target == matrix[row][m]:
                return True
            elif matrix[row][m] < target:
                l = m + 1
            else:
                r = m - 1
        
        return False





