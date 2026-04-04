class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        currMax, currMin = 1, 1

        for n in nums:
            tmp = currMax * n
            currMax = max(currMax * n, currMin * n, n)
            currMin = min(tmp, currMin * n, n)
            res = max(res, currMax)
        return res

        


# [1,2,-3,4,-2]
# currMax = 1, currMin = 1, res = 1
# currMax = 2, currMin = 1, res = 2
# currMax = -3, currMin = -6, res = 2
# currMax = 4, currMin = -24, res = 4
# currMax = 48, currMin = -8, res =48