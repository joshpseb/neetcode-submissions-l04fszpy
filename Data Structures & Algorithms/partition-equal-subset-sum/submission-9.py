class Solution: #neet
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        target = total // 2

        dp = set()
        dp.add(0)
        
        for num in nums:
            nextDP = dp.copy()
            for t in nextDP:
                dp.add(t + num)
        
        return True if target in dp else False
        