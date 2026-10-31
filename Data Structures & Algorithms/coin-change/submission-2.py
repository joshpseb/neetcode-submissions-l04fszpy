class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #bottom up: 

        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if c <= a:
                    dp[a] = min(dp[a], 1 + dp[a - c])
        
        res = dp[amount]
        return res if res != float('inf') else -1