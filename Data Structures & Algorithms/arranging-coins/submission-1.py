class Solution:
    def arrangeCoins(self, n: int) -> int:
        l, r = 0, math.ceil(n / 2)
        res = 0

        while l <= r:
            m = (l + r) // 2

            total = m * (m + 1) // 2

            if total <= n:
                l = m + 1
                res = max(res, m)
            else:
                r = m - 1
            
        return res