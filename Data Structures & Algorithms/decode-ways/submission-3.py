class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        mem = [-1] * len(s)

        def dfs(i):
            if i == len(s):
                return 1
            if s[i] == "0":
                return 0
            
            if mem[i] == -1:
                if i + 2 <= n and int(s[i:i + 2]) <= 26:
                    mem[i] = dfs(i + 2) + dfs(i + 1)
                else:
                    mem[i] = dfs(i + 1)
            return mem[i]
            

        return dfs(0) 
        