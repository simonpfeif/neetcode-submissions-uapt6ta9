class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        upper = max(piles)
        lower = 1
        res = upper

        while lower <= upper:
            k = (upper + lower) // 2

            time = self.eatBananas(k, piles)
            if time <= h:
                res = min(res, k)
                upper = k - 1
            else:
                lower = k + 1

        return res
    
    def eatBananas(self, k, piles):
        time = 0
        for pile in piles:
            time += math.ceil(pile / k)
        
        return time