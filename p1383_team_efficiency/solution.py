import heapq
from typing import List

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        engineers = []
        for ev, sv in zip(efficiency, speed):
            engineers.append([ev, sv])
        engineers.sort(reverse=True)
        
        result, totalSpeed = 0, 0
        minHeap = []
        for ev, sv in engineers:
            if len(minHeap) == k:
                totalSpeed -= heapq.heappop(minHeap)
            totalSpeed += sv
            heapq.heappush(minHeap, sv)
            result = max(result, ev * totalSpeed)

        return result % (10 ** 9 + 7)