class Solution:
    def myPow(self, x: float, n: int) -> float:
        negative = False
        if n < 0:
            n = -n
            negative = True
        res = 1
        for _ in range(n):
            res *= x
        return 1 / res if negative else res