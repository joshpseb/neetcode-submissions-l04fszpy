class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        rangeSum = 0
        for i in range(len(nums) + 1):
            rangeSum += i
        return rangeSum - sum(nums)