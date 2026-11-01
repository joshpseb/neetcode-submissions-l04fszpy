class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        #bottom up approach: work up from sum of 0 to sum of target

        total = sum(nums)

        if total % 2 == 1:
            return False
        
        target = total // 2

        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            for i in range(len(dp) - 1, -1, -1):
                if dp[i] and num + i < len(dp):
                    dp[num + i] = True
        return dp[-1]
