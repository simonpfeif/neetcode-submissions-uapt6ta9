class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shift = 0
        while left != right:
            shift += 1
            left >>= 1
            right >>= 1
        
        return left << shift