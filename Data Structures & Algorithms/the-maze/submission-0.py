class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        ROWS, COLS = len(maze), len(maze[0])
        seen = set()

        def dfs(r, c):
            if [r, c] == destination:
                return True

            if (r,c) in seen:
                return False

            seen.add((r, c))

            for dr, dc in directions:
                row, col = r, c
                while 0 <= row + dr < ROWS and 0 <= col + dc < COLS and maze[row + dr][col + dc] == 0:
                    row += dr
                    col += dc
                
                if dfs(row, col):
                    return True
            return False
        
        return dfs(start[0], start[1])