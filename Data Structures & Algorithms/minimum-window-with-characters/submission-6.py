class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l, count, res = 0, 0, ""
        countMap, window = {}, {}
        for c in t:
            countMap[c] = 1 + countMap.get(c, 0)
        

        for r in range(len(s)):
            c = s[r]
            if c in countMap:
                window[c] = 1 + window.get(c, 0)
                if window[c] == countMap[c]:
                    count += 1

            while count == len(countMap):
                res = s[l:r + 1] if (r - l + 1) < len(res) or res == "" else res

                if s[l] in countMap:
                    window[s[l]] -= 1
                    if window[s[l]] < countMap[s[l]]:
                        count -= 1
                l += 1

        return res