class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        memo = [[-1] * 2 for _ in range(n)]


        def dfs(i, flag):
            if i >= (n - flag):
                return 0

            if memo[i][flag] == -1:
                memo[i][flag] = max(dfs(i + 1, flag), nums[i] + dfs(i + 2, flag))

            return memo[i][flag]

        return max(dfs(0, 1), dfs(1, 0))