class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique = sorted(set(nums))
        print(unique)
        if not nums:
            return 0
        maxSeq = 1
        seq = 1
        for num in unique:
            if num - 1 in unique:
                seq += 1
                maxSeq = max(seq, maxSeq)
            else:
                seq = 1
        return maxSeq
            