class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        left = nums[0]
        for i in range(1, n):
            res[i] = left
            left *= nums[i]
        
        right = nums[n - 1]
        for j in range(n - 2, -1, -1):
            res[j] *= right
            right *= nums[j]
        
        return res