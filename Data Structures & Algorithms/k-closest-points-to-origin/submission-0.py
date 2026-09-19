class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            dist = (x**2 + y**2)
            heapq.heappush(heap, [-dist, [x, y]])
            while len(heap) > k:
                heapq.heappop(heap)
        return [point for dist, point in heap]