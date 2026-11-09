class Solution:
    def trap(self, height: List[int]) -> int:
        l, r, res = 0, len(height) - 1, 0
        heightL, heightR = height[l], height[r]

        while l < r:
            if heightL < heightR:
                l += 1
                heightL = max(heightL, height[l])
                res += max(0, min(heightL, heightR) - height[l])
            else:
                r -= 1
                heightR = max(heightR, height[r])
                res += max(0, min(heightL, heightR) - height[r])
        return res