class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # memoization
        memo = {}
        
        def dfs(i, remaining):
            if (i, remaining) in memo:
                return memo[(i, remaining)]
                
            if i >= len(coins):
                return 0
            if remaining < 0:
                return 0
            if remaining == 0:
                return 1
            
            memo[(i, remaining)] = dfs(i, remaining - coins[i]) + dfs(i + 1, remaining)
            return memo[(i, remaining)]

        return dfs(0, amount)