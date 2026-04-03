class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        prefix = [1] * n
        for i in range(1, n):
            prefix[i] = nums[i-1] * prefix[i-1]

        postfix = [1] * n
        for i in range(n - 2, -1, -1):
            postfix[i] = nums[i + 1] * postfix[i + 1]
        
        res = [0] * n
        for i in range(n):
            res[i] = prefix[i] * postfix[i]
        return res