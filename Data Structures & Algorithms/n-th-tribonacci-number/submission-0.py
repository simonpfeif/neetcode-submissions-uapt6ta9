class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1

        T0, T1, T2 = 0, 1, 1
        i = 2
        TNext = 0
        while i < n:
            i += 1
            TNext = T0 + T1 + T2
            T0, T1, T2 = T1, T2, TNext
        
        return TNext
