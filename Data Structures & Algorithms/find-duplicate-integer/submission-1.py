class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        prev = float("-inf")
        for n in nums:
            if n == prev:
                return n
            else:
                prev = n
        return -1