class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # bottom up dp
        # get the val of dp[r][c] by adding vals of dp[r-1][c] and dp [r][c-1]
        # time and space O(mn)

        # optimized version that doesn't store every row and col, only relevant prev vals needed to calc current pos
        # the entire top row and left col are all 1s
        # if calculating row by row, only need to store prev row and update it

        dp = [1] * n

        for i in range(1, m):
            for j in range(1, n):
                dp[j] = dp[j] + dp[j - 1]

        return dp[n - 1]