class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        cnts = Counter(s)
        odd_cnt = 0

        for c, cnt in cnts.items():
            if cnt % 2:
                odd_cnt += 1
                if odd_cnt > 1:
                    return False
        
        return True