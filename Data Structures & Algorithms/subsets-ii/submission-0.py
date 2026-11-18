class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # start with []
        # dfs: choose to skip or keep nums[i]
        # 
        nums.sort()
        subsets = set()

        def dfs(i, currSet):
            if i == len(nums):
                subsets.add(tuple(currSet))
                return
            
            # skip: keep currSet, increment i
            dfs(i + 1, currSet)

            # add: add candidates[i], increment i
            currSet.append(nums[i])
            dfs(i + 1, currSet)
            currSet.pop()


        dfs(0, [])

        subsets = list(subsets)
        for s in subsets:
            s = list(s)
        print(subsets)
        return subsets