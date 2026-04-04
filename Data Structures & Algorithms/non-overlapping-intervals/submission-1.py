class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        prevEnd = intervals[0][1]
        res = 0

        for i in range(1, len(intervals)):
            if prevEnd > intervals[i][0]:
                # check end of last is greater than start of curr
                res += 1
                prevEnd = min(prevEnd, intervals[i][1])
            else:
                prevEnd = intervals[i][1]
            
        return res