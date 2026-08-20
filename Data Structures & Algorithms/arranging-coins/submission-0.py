class Solution:
    def arrangeCoins(self, n: int) -> int:
        res = 0
        total = 0
        
        for i in range(1, n + 1):
            if total + i > n:
                return res
            
            total += i
            res += 1
        
        return res
