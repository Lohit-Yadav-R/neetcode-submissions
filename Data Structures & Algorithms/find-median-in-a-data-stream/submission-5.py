class MedianFinder:

    def __init__(self):
        self.maxh = []
        self.minh = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxh, -num)
        heapq.heappush(self.minh, -heapq.heappop(self.maxh))
        if len(self.minh) > len(self.maxh):
            heapq.heappush(self.maxh, -heapq.heappop(self.minh))

    def findMedian(self) -> float:
        if len(self.maxh) > len(self.minh):
            return -self.maxh[0] / 1
        return (-self.maxh[0] + self.minh[0]) / 2
