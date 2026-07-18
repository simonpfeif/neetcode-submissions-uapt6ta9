class Solution:
    def countOdds(self, low: int, high: int) -> int:
        # first + diff // 2
        diff = high - low

        if high == low:
            return low % 2

        if diff % 2: # odd
            return (high - low) // 2 + 1

        return low % 2 + (high - low) // 2