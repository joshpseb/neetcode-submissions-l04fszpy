class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # bottom up
        # array n x amount
        # start at n - 1, remaining = 0
        # dp[i][remaining] = dp[i][remaining - coins[i]] + dp[i + 1][remaining]

        n = len(coins)
        dp = [[0] * (amount + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = 1

        for i in range(n - 1, -1, -1):
            for remaining in range(1, amount + 1):
                dp[i][remaining] = dp[i][remaining - coins[i]] + dp[i + 1][remaining]
        return dp[0][amount]