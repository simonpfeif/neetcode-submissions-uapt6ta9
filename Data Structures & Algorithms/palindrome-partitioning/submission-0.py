class Solution:
    def isPalindrome(self, s, l, r):
        while (l < r):
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    def partition(self, s: str) -> List[List[str]]:
        res, curr = [], []
        def dfs(i, j):
            if (i >= len(s)):
                if j == i:
                    res.append(curr.copy())
                return

            if self.isPalindrome(s, j, i):
                curr.append(s[j : i + 1])
                dfs(i + 1, i + 1)
                curr.pop()
            dfs(i + 1, j)
        dfs(0, 0)
        return res
    