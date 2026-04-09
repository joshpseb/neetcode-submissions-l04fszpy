class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        out = defaultdict(list)
        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                diff = nums[j] + nums[k]
                if nums[i] + diff > 0:
                    k -= 1
                elif nums[i] + diff < 0:
                    j += 1
                else:
                    if [nums[i], nums[j], nums[k]] not in res:
                        res.append([nums[i], nums[j], nums[k]])
                    j += 1
        return res