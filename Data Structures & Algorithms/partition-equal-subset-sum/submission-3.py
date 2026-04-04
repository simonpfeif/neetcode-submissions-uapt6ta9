class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        if target % 2 == 1: return False
        target = target // 2
        dp = set()
        dp.add(0)

        for i in range(len(nums) - 1, -1, -1):
            nextDp = set()
            for t in dp:
                if (t + nums[i]) == target:
                    return True
                nextDp.add(t)
                nextDp.add(t + nums[i])
            dp = nextDp
            
        return False
        # total = sum(nums)
        # if total % 2 == 1: return False

        # def dfs(curr, i):
        #     if curr == (total - curr):
        #         return True
        #     if i >= len(nums) or curr > (total - curr):
        #         return False
            
        #     return dfs(curr, i + 1) or dfs(curr + nums[i], i + 1)

        # return dfs(0, 0)