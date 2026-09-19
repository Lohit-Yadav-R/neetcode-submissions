class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        heap = [-stone for stone in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            stone1 = -heapq.heappop(heap)
            stone2 = -heapq.heappop(heap)
            if stone1 == stone2:
                continue
            newStone = stone1 - stone2
            heapq.heappush(heap, -newStone)
        return -heap[0] if heap else 0