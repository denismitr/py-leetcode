class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        mod = 10**9 + 7
        dp = {}

        def dfs(length):
            if length > high:
                return 0
            if length in dp:
                return dp[length]
            
            res = 1 if length >= low else 0
            res += dfs(length + zero) + dfs(length + one)
            dp[length] = res % mod
            return dp[length]
        
        return dfs(0)