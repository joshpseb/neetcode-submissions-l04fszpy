class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s = 0
        for i in range(len(nums)):
            s += i - nums[i]
        return s + len(nums)