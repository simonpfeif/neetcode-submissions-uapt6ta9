class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)

        def dfs(i):
            if i == len(s):
                return 1
            if s[i] == "0":
                return 0
            
            if i + 2 <= n and int(s[i:i + 2]) <= 26:
                return dfs(i + 2) + dfs(i + 1)
            else:
                return dfs(i + 1)

        return dfs(0) 
        