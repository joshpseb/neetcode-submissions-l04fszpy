class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []

        for p in points:
            x, y = p[0], p[1]
            heapq.heappush_max(maxHeap, (math.sqrt((x)**2 + (y)**2), p))
            if len(maxHeap) > k:
                heapq.heappop_max(maxHeap)
        return list(x[1] for x in maxHeap)