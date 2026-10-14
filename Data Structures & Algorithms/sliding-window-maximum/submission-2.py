class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        out = []
        maxHeap = []

        for i in range(k - 1):
            heapq.heappush_max(maxHeap, (nums[i], i))
        
        for i in range(len(nums) - k + 1):
            heapq.heappush_max(maxHeap, (nums[i + k - 1], i + k - 1))
            while True:
                if maxHeap[0][1] >= i and maxHeap[0][1] < i + k:
                    out.append(maxHeap[0][0])
                    break
                else:
                    heapq.heappop_max(maxHeap)
        return out