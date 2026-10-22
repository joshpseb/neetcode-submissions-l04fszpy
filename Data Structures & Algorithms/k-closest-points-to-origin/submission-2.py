class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            dist = (x**2 + y**2)
            heapq.heappush(heap, [dist, x, y])
        out = []
        for _ in range(k):
            dist, x, y = heapq.heappop(heap)
            out.append([x, y])
        return out

            