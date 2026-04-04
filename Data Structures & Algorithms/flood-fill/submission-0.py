class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original_color = image[sr][sc]
        ROWS, COLS = len(image), len(image[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = [[False] * COLS for _ in range(ROWS)]

        def dfs(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or visited[r][c] or image[r][c] != original_color:
                return
            
            image[r][c] = color
            print(image)
            visited[r][c] = True
            for dr, dc in directions:
                dfs(r + dr, c + dc)
        
        dfs(sr, sc)
        return image
            