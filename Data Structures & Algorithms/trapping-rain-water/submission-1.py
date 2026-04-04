class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        l, r, res = 0, len(height) - 1, 0
        leftH, rightH = height[l], height[r]

        while l < r:
            if leftH <= rightH:
                l += 1
                leftH = max(leftH, height[l])
                res += leftH - height[l]
            else:
                r -= 1
                rightH = max(rightH, height[r])
                res += rightH - height[r]
        return res