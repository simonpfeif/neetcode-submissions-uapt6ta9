class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        j = 0
        n = len(t)

        for c in s:
            if c == t[j]:
                j += 1
                if j == n:
                    return 0
        
        return len(t) - j 

        