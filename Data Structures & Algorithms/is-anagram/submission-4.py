class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        cnts1 = Counter(s)
        cnts2 = Counter(t)

        return cnts1 == cnts2
        
