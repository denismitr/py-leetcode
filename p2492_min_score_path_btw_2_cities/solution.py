from collections import defaultdict
from typing import List


class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adj = defaultdict(list)
        for src, dest, distance in roads:
            adj[src].append((dest, distance))
            adj[dest].append((src, distance))

        result = float("inf")
        visited = set()
        def dfs(i):
            if i in visited:
                return
            visited.add(i)
            nonlocal result
            for neighbour, distance in adj[i]:
                result = min(result, distance)
                dfs(neighbour)

        dfs(1)
        return result