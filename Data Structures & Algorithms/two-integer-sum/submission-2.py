class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for idx, num in enumerate(nums):
            diff = target - num
            if diff in hash:
                return [hash[diff], idx]
            else:
                hash[num] = idx