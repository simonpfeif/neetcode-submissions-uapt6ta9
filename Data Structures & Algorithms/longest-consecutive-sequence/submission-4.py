class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet = set(nums)
        res = 0

        for num in nums:
            if num - 1 not in hashSet:
                cnt = 0
                while num in hashSet:
                    cnt += 1
                    num += 1
                res = max(res, cnt)
        return res