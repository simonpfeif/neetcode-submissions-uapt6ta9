class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        LIS = [1] * n

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        
        return max(LIS)

        # memo = {}

        # def dfs(last, i):
        #     if i >= len(nums):
        #         return 0
        #     if (last, i) not in memo:
        #         if last == -1 or nums[last] < nums[i]:
        #             memo[(last, i)] = max(1 + dfs(i, i + 1), dfs(last, i + 1))
        #         else:
        #             memo[(last, i)] = dfs(last, i + 1)

        #     return memo[(last, i)]
        
        # return dfs(-1, 0)