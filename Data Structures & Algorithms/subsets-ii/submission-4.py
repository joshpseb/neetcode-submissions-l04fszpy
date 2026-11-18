class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # start with []
        # dfs: choose to skip or keep nums[i]
        # 
        nums.sort()
        subsets = []
        #subsets = set()

        def dfs(i, currSet):
            if i == len(nums):
                subsets.append(currSet.copy())
                return

            # add: add candidates[i], increment i
            currSet.append(nums[i])
            dfs(i + 1, currSet)
            currSet.pop()

            # skip: keep currSet, increment i until new val
            while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                i += 1
            dfs(i + 1, currSet)


        dfs(0, [])

        #subsets = [list(s) for s in subsets]
        return subsets