class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        #solution 1 with memoization
        memo = {}

        total = sum(nums)

        if total % 2 == 1:
            return False
        
        target = total // 2

        def dfs(i, remaining):
            if (i, remaining) in memo:
                return memo[(i, remaining)]

            if remaining == 0:
                return True
            if i >= len(nums):
                return False
            
            memo[(i, remaining)] = dfs(i + 1, remaining) or dfs(i + 1, remaining - nums[i])
            return memo[(i, remaining)]
        
        return dfs(0, target)