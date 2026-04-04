class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}

        def dfs(last, i):
            if i >= len(nums):
                return 0
            if (last, i) not in memo:
                if last == -1 or nums[last] < nums[i]:
                    memo[(last, i)] = max(1 + dfs(i, i + 1), dfs(last, i + 1))
                else:
                    memo[(last, i)] = dfs(last, i + 1)

            return memo[(last, i)]
        
        return dfs(-1, 0)