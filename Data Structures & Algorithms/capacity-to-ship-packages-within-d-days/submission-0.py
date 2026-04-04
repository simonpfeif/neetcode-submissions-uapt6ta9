class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)

        def canFinish(capacity):
            ships, currCap = 1, capacity
            for w in weights:
                if currCap < w:
                    ships += 1
                    if ships > days:
                        return False
                    currCap = capacity
                currCap -= w
            return True
        
        capacity = r
        while l <= r:
            m = (l + r) // 2
            
            if canFinish(m):
                capacity = min(capacity, m)
                r = m - 1
            else:
                l = m + 1
        return capacity