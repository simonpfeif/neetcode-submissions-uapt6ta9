class Solution:
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
        ROWS, COLS = len(maze), len(maze[0])
        directions = [[1, 0, "d"], [0, -1, "l"], [0, 1, "r"], [-1, 0, "u"]]

        dist_map = {}
        pq = [(0, "", ball[0], ball[1])] # dist, path, row, col

        while pq:
            dist, path, row, col = heapq.heappop(pq)

            if (row, col) in dist_map and (dist, path) >= dist_map[(row, col)]:
                continue
            
            dist_map[(row, col)] = (dist, path)
            if [row, col] == hole: continue

            for dx, dy, d_char in directions:
                r, c = row, col
                cnt = 0

                while 0 <= r + dx < ROWS and 0 <= c + dy < COLS and maze[r + dx][c + dy] == 0:
                    r += dx
                    c += dy
                    cnt += 1
                    if [r, c] == hole:
                        break
                
                if cnt > 0:
                    heapq.heappush(pq, (dist + cnt, path + d_char, r, c))
        
        return dist_map.get((hole[0], hole[1]), (float('inf'), "impossible"))[1]