class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # bottom up dp
        # use a 2d array size (m + 1) * (n + 1), all vals 0
        # using solution 2 for the base idea, start at m-1, n-1.
        # if chars equal, move diagonally and add 1
        # if not equal, choose max of i+1,j and i,j+1 and move in that direction

        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])
        
        return dp[0][0]
