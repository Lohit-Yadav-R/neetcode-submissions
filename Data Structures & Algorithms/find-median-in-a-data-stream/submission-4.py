import heapq

class MedianFinder:

    def __init__(self):
        self.small = []  # Max-heap (store negated values)
        self.large = []  # Min-heap

    def addNum(self, num: int) -> None:
        # Step 1: Push to max-heap (small), then move the largest element to min-heap (large)
        heapq.heappush(self.small, -num)
        heapq.heappush(self.large, -heapq.heappop(self.small))

        # Step 2: Maintain size property (small can have at most 1 more element than large)
        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        return (-self.small[0] + self.large[0]) / 2.0