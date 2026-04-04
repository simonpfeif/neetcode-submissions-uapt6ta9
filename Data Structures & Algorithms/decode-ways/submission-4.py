class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [1] * (len(s) + 1)

        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]
            
            if i + 1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"):
                dp[i] += dp[i + 2]
        return dp[0]

        # n = len(s)
        # mem = [-1] * len(s)

        # def dfs(i):
        #     if i == len(s):
        #         return 1
        #     if s[i] == "0":
        #         return 0
            
        #     if mem[i] == -1:
        #         if i + 2 <= n and int(s[i:i + 2]) <= 26:
        #             mem[i] = dfs(i + 2) + dfs(i + 1)
        #         else:
        #             mem[i] = dfs(i + 1)
        #     return mem[i]
            

        # return dfs(0) 
        