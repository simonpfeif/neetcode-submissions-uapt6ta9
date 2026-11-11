class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        max_freq = 0
        l = 0
        res = 0

        for r in range(len(s)):
            counts[s[r]] = 1 + counts.get(s[r], 0)
            max_freq = max(max_freq, counts[s[r]])

            while 1 + r - l - max_freq > k:
                # shrink window. Never reduce max_feq b/c it is not necessary
                counts[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)

        return res

