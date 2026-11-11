class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        letters = [0] * 26
        for c in s1:
            letters[ord(c) - ord('a')] += 1
        
        l = 0
        for r in range(len(s2)):
            idx = ord(s2[r]) - ord('a')

            letters[idx] -= 1

            while letters[idx] < 0:
                # move window
                letters[ord(s2[l]) - ord('a')] += 1
                l += 1
            
            if r - l + 1 == len(s1):
                return True
        
        return False

        