class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # use memoization: when some amount is left, the min numCoins for that amount only needs to be calculated once. in the rest of the decision tree, just need to pull that info from a memo/hashmap

        memo = {}

        def dfs(amount):
            if amount in memo: # checks if min has been calculated for this amount
                return memo[amount]

            if amount == 0:
                return 0
            if amount < 0:
                return float('inf')
            
            minCoins = float('inf')

            for c in coins:
                minCoins = min(minCoins, 1 + dfs(amount - c))
            
            memo[amount] = minCoins
            return minCoins
            
        res = dfs(amount)
        return res if res != float('inf') else -1