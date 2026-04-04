class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        l = 0
        res = 0

        for r in range(len(s)):
            if s[r] in mp:
                l = max(mp[s[r]] + 1, l)
            mp[s[r]] = r
            res = max(res, r - l + 1)
        return res
        # window = set()
        # l = 0
        # res = 0

        # for r in range(len(s)):
        #     while s[r] in window:
        #         window.remove(s[l])
        #         l += 1
        #     window.add(s[r])
        #     res = max(res, len(window))
        
        # return res