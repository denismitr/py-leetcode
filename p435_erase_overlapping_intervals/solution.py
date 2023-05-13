from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        result = 0
        prevEnd = intervals[0][1]
        for start, end in intervals[1:]:
            if start >= prevEnd: # does not overlap with previous interval
                prevEnd = end
            else:
                result += 1
                prevEnd = min(end, prevEnd)
        return result
