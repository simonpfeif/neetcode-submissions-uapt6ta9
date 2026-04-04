class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = 0
        res = nums[0]
        for num in nums:
            if sum < 0:
                sum = 0
            sum += num
            res = max(res, sum)
        return res

# 1 1 1 -4 2