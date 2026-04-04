class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        n = self.sumOfSquares(n)
        print(n)

        while n not in seen:
            if n == 1:
                return True
            seen.add(n)
            n = self.sumOfSquares(n)
        return False

    
    def sumOfSquares(self, n):
        res = 0
        while n:
            digit = n % 10
            res += digit ** 2
            n = n // 10
        return res