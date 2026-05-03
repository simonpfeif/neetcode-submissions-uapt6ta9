class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        ROWS, COLS = len(maze), len(maze[0])
        dist = [[float('inf')] * COLS for _ in range(ROWS)]
        dist[start[0]][start[1]] = 0
        pq = [(0, start[0], start[1])]

        while pq:
            d, r, c = heapq.heappop(pq)
            if d > dist[r][c]:
                continue
            if [r, c] == destination:
                return d

            for dr, dc in directions:
                row, col = r, c
                traveled = 0
                while 0 <= row + dr < ROWS and 0 <= col + dc < COLS and maze[row + dr][col + dc] == 0:
                    row += dr
                    col += dc
                    traveled += 1
                
                if d + traveled < dist[row][col]:
                    dist[row][col] = d + traveled
                    heapq.heappush(pq, (dist[row][col], row, col))
        
        res = dist[destination[0]][destination[1]]
        return res if res != float('inf') else -1