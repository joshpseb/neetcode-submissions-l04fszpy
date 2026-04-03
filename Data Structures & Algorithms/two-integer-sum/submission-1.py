class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for idx, num in enumerate(nums):
            if target - num in hash:
                return [hash[target-num], idx]
            else:
                hash[num] = idx