class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s = set(nums)
        print(s)

        for n in range(len(nums) + 1):
            if n not in s:
                return n
        return -1

