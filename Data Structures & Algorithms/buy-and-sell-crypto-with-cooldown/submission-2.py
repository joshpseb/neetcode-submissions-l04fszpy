class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # bottom up dp
        # have 2 rows for buy and sell
        n = len(prices)

        dp = [[0] * 2 for _ in range(n + 2)]
        #first row buy, second row sell

        # (i, "buy") = max(-prices[i] + dfs(i + 1, "sell"), dfs(i + 1, "buy"))
        # (i, "sell") = max(prices[i] + dfs(i + 2, "buy"), dfs(i + 1, "sell"))

        for i in range(n - 1, -1, -1):
            dp[i][0] = max(-prices[i] + dp[i + 1][1], dp[i + 1][0])
            dp[i][1] = max(prices[i] + dp[i + 2][0], dp[i + 1][1])
        
        return dp[0][0]