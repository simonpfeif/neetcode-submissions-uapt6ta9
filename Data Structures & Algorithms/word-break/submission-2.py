class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        hashset = set(wordDict)
        memo = {}

        def dfs(l, r):
            if r >= len(s):
                return l == r
            if (l, r) not in memo:
                if s[l:r + 1] in hashset:
                    memo[(l, r)] = dfs(r + 1, r + 1) or dfs(l, r + 1)
                else:
                    memo[(l, r)] = dfs(l, r + 1)
            return memo[(l, r)]
        
        return dfs(0, 0)
        