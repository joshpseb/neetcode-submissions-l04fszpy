class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1 
        # count sorted by value, then spliced to get first k key-value pairs
        count = sorted(count.items(), key = lambda x: x[1], reverse = True)[:k]
        return [num for num, ct in count]