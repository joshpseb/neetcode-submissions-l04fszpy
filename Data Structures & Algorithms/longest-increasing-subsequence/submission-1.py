class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #brute force to memoization

        memo = {}

        def dfs(i, prev):
            if i >= len(nums):
                return 0
            if (i, prev) in memo:
                return memo[(i, prev)]
            
            include = float('-inf')
            skip = dfs(i + 1, prev)
            if nums[i] > prev:
                include = 1 + dfs(i + 1, nums[i])
            
            memo[(i, prev)] = max(include, skip)
            return memo[(i, prev)]
        
        return dfs(0, float('-inf'))