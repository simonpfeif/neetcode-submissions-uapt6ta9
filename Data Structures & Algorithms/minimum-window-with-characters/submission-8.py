class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        num_found = 0
        cnts = Counter(t)
        target = len(cnts)
        res = ""

        l = 0

        for r in range(len(s)):
            if s[r] in cnts:
                cnts[s[r]] -= 1
                if cnts[s[r]] == 0:
                    num_found += 1
            
            while s[l] not in cnts and l < r:
                l += 1

            while num_found == target:
                if s[l] in cnts:
                    cnts[s[l]] += 1
                    
                    if cnts[s[l]] > 0:
                        num_found -= 1

                    if r - l + 1 < len(res) or res == "":
                        res = s[l:r + 1]
                l += 1


        return res
                