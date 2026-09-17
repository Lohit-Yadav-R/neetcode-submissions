class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            s1 = -(heapq.heappop(heap))
            s2 = -(heapq.heappop(heap))
            if s1 == s2:
                continue
            newS = s1 - s2
            heapq.heappush(heap, -newS)
        return -heap[0] if heap else 0