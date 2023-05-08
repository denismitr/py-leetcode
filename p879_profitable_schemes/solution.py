from collections import defaultdict


class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]):
        mod = 10**9 + 7  # really large prime number

        dp = {}

        # i - index we are
        # n - how many group members are left 
        # p - current profit
        def dfs(i, n, p):
            if i == len(group):
                return 1 if p >= minProfit else 0

            if (i, n, p) in dp:
                return dp[(i, n, p)]

            dp[(i, n, p)] = dfs(i + 1, n, p)  # skipped index i
            if n - group[i] >= 0:
                dp[(i, n, p)] += dfs(i + 1, n - group[i], p + profit[i]) % mod


            return dp[(i, n, p)]


        return dfs(0, n, 0)

    def profitableSchemesTab(self, n: int, minProfit: int, group: List[int], profit: List[int]):
        mod = 10**9 + 7
        dp = defaultdict(int)

        for m in range(n + 1):
            dp[len(group), m, minProfit] = 1
            
        for i in range(len(group) - 1, -1, -1):
            for m in range(n + 1):
                for p in range(minProfit + 1):
                    dp[(i, m, p)] = dp[(i+1, m, p)]
                    if m + group[i] <= n:
                        dp[(i, m, p)] += dp[(i + 1, m + group[i], min(minProfit, p + profit[i]))] % mod

        return dp[(0, 0, 0)] % mod
