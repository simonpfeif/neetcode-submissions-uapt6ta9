class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counts = Counter(text)
        res = float('inf')

        for char in "balloon":
            cnt = counts[char]
            if char == 'o' or char == 'l':
                res = min(res, cnt // 2)
            else:
                res = min(res, cnt)
        
        return res if res != float('inf') else 0
