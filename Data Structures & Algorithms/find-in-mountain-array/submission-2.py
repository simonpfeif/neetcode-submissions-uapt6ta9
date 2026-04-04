class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        # """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

        l = 0
        n = mountainArr.length()
        r = n - 1
        cache = {}
        peak = -1

        def get(i):
            if i not in cache:
                cache[i] = mountainArr.get(i)
            return cache[i]

        # find peak
        while l <= r:
            m = (l + r) // 2

            el = get(m)
            el_left = get(m - 1)
            el_right = get(m + 1)
            print(el_left, el, el_right)

            if el_left < el > el_right:
                peak = m
                break
            elif el_left > el:
                r = m - 1
            else:
                l = m + 1


        # binary search on left
        l, r = 0, peak
        while l <= r:
            m = (l + r) // 2

            el = get(m)
            if el == target:
                return m
            elif el < target:
                l = m + 1
            else:
                r = m - 1

        # binary search on right
        l, r = peak + 1, n - 1
        while l <= r:
            m = (l + r) // 2

            el = get(m)
            if el == target:
                return m
            elif el > target:
                l = m + 1
            else:
                r = m - 1
        
        return -1