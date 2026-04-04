class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def dfs(picked, curr):
            if len(curr) == n:
                res.append(curr.copy())
            for i in range(n):
                if not picked[i]:
                    picked[i] = True
                    curr.append(nums[i])
                    dfs(picked, curr)

                    picked[i] = False # backtrack step
                    curr.pop()

            
        dfs([False] * n, [])
        return res