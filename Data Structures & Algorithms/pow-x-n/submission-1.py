class Solution:
    def myPow(self, x: float, n: int) -> float:

        def recursion(x, n):
            if x == 0:
                return 0
            if n == 0:
                return 1
            res = recursion(x * x, n // 2)
            return x * res if n % 2 == 1 else res
        
        res = recursion(x, abs(n))
        return res if n > 0 else 1 / res