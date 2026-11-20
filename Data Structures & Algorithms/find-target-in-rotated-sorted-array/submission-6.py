class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m
            
            # left
            if nums[l] < nums[m] and nums[l] <= target < nums[m]:
                # pivot not in this subarray
                r = m - 1
            elif nums[l] > nums[m] and (nums[l] <= target or target < nums[m]):
                #pivot in this subarray
                r = m - 1
            else:
                #right side
                l = m + 1
        
        return -1
