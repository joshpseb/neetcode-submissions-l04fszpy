class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # bottom up dp optimized
        # time O(mn) space O(n)

        # optimized version that doesn't store every row and col, only relevant prev vals needed to calc current pos
        # the entire top row and left col are all 1s
        # if calculating row by row, only need to store prev row and update it

        dp = [1] * n

        for i in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j - 1]

        return dp[n - 1]