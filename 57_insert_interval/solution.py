from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                result.append(newInterval) # newInterval is to the left of intervals[i]
                return result + intervals[i:] # we can return early
            elif newInterval[0] > intervals[i][1]:
                result.append(intervals[i]) # newInterval is to the right of intervals[i]   
            else: #overlap
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        return result + [newInterval]