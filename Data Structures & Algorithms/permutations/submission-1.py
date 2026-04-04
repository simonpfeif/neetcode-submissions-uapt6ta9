class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.backtrack([False] * len(nums), [], nums)
        return self.res

    def backtrack(self, picked: List[bool], curr: List[int], nums: List[int]):
            if len(curr) == len(nums):
                self.res.append(curr[:])
                return

            for i in range(len(nums)):
                if not picked[i]:
                    picked[i] = True
                    curr.append(nums[i])
                    self.backtrack(picked, curr, nums)

                    picked[i] = False # backtrack step
                    curr.pop()