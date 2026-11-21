class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        a = 0
        for i in range(len(nums) + 1):
            a ^= i
        
        for n in nums:
            a ^= n
        
        return a
