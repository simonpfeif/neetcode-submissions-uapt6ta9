class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        dp = defaultdict(int)
        dp[0] = 1 # element 0, sum 0 -> 1 way
                     # 1 way to sum to zero with first 0 elements of nums
        
        for i in range(len(nums)):
            nextDp = defaultdict(int)
            for cur_sum, count in dp.items():
                nextDp[cur_sum + nums[i]] += count
                nextDp[cur_sum - nums[i]] += count

            dp = nextDp

        return dp[target]
        
        # memo = {}

        # def dfs(i, t):
                
        #     if i == len(nums):
        #         return 1 if t == target else 0
            
        #     if (i, t) in memo:
        #         return memo[(i, t)]

        #     memo[(i, t)] = dfs(i + 1, t + nums[i]) + dfs(i + 1, t - nums[i])
        #     return memo[(i, t)]

        # return dfs(0, 0)