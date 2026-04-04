class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()

        def dfs(curr, prev, hash_set):
            r = curr[0]
            c = curr[1]

            if r < 0 or r >= len(heights) or c < 0 or c >= len(heights[0]) or curr in hash_set or heights[r][c] < heights[prev[0]][prev[1]]:
                return
            
            hash_set.add(curr)
            dfs((r, c + 1), curr, hash_set)
            dfs((r, c - 1), curr, hash_set)
            dfs((r + 1, c), curr, hash_set)
            dfs((r - 1, c), curr, hash_set)
        
        for r in range(len(heights)):
            for c in range(len(heights[r])):
                if r == 0:
                    dfs((r, c), (r, c), pacific)
                if c == 0:
                    dfs((r,c), (r, c), pacific)
                if r == len(heights) - 1:
                    dfs((r, c), (r, c), atlantic)
                if c == len(heights[r]) - 1:
                    dfs((r, c), (r, c), atlantic)
            
        
        res = []
        for cell in atlantic:
            if cell in pacific:
                res.append([cell[0], cell[1]])
        return res




