class Solution:
    def rob(self, nums: List[int]) -> int:
        #optimize bottom up to O(1) space by only storing the two dp needed to get curr house

        dp1 = 0
        dp2 = 0

        for i in range(len(nums) - 1, -1, -1):
            temp = dp1
            dp1 = max(nums[i] + dp2, dp1)
            dp2 = temp
        
        return dp1