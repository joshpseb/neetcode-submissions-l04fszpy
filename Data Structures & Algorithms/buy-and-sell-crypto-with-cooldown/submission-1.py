class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # memoized

        memo = {}

        def dfs(i, state): # returns max profit starting at i based on state chosen, state represents ability to buy or sell, not that you need to do one or the other
            if (i, state) in memo:
                return memo[(i, state)]

            if i >= len(prices):
                return 0
            if i == len(prices) - 1 and state == "buy":
                return 0
            if state == "buy": # buy today or buy later, choose max
                memo[(i, state)] = max(-prices[i] + dfs(i + 1, "sell"), dfs(i + 1, "buy"))
                return memo[(i, state)]
            if state == "sell": # sell today (skip a day for buy) or sell later, choose max
                memo[(i, state)] = max(prices[i] + dfs(i + 2, "buy"), dfs(i + 1, "sell"))
                return memo[(i, state)]

        return dfs(0, "buy")