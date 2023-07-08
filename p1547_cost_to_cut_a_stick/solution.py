class Solution():
    def minCost(self, n: int, cuts: List[int]) -> int:
        seen = {}

        def dfs(l, r):
            if r - l == 1:
                return 0
            if (l, r) in seen:
                return seen[(l, r)]
            
            res = float("inf")
            for c in cuts:
                if l < c < r:
                    res= min(res, (r - l) + dfs(l, c) + dfs(c, r))
            seen[(l, r)] = 0 if res == float("inf") else res
            return seen[(l, r)]

        return dfs(0, n)
