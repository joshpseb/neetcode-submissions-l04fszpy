class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # bottom up dp
        # get the val of dp[r][c] by adding vals of dp[r-1][c] and dp [r][c-1]

        dp = [[0] * n for i in range(m)]
        dp[0][0] = 1

        for i in range(m):
            for j in range(n):
                if i > 0 and j > 0:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
                elif i > 0 and j <= 0:
                    dp[i][j] = dp[i - 1][j]
                elif i <= 0 and j > 0:
                    dp[i][j] = dp[i][j - 1]
        return dp[m - 1][n - 1]

        