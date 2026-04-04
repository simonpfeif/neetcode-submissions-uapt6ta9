class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        q = deque()
        directions = [(0,1), (1,0), (-1,0), (0,-1)]

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1: 
                    fresh += 1
        
        mins = 0
        while fresh > 0 and q:
            for _ in range(len(q)):
                r, c = q.popleft()

                for d in directions:
                    row = d[0] + r
                    col = d[1] + c

                    if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] != 1:
                        continue
                    
                    grid[row][col] = 2
                    fresh -= 1
                    q.append((row, col))

            mins += 1
        
        return mins if fresh == 0 else -1

