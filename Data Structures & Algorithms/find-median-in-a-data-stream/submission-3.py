class MedianFinder:

    def __init__(self):
        self.heaps = [None, [], []] # 0th index is for minheap, 1st index for maxheap.
        self.flag = 0

    def addNum(self, num: int) -> None:
        if not self.heaps[1]:
            heapq.heappush(self.heaps[1], -num)
            heapq.heappush(self.heaps[-1], num)
            self.flag = 1 - self.flag # 1 means same element at the top of both heaps, 0 means different elements.
            return
        pushIdx = 1 if num <= -self.heaps[1][0] else -1
        sign = -pushIdx
        if self.flag:
            heapq.heappop(self.heaps[pushIdx])
            heapq.heappush(self.heaps[pushIdx], num * sign)
        else:
            if -self.heaps[1][0] <= num <= self.heaps[-1][0]:
                heapq.heappush(self.heaps[1], -num)
                heapq.heappush(self.heaps[-1], num)
            else:
                pullIdx = -pushIdx
                heapq.heappush(self.heaps[pullIdx], -self.heaps[pushIdx][0])
                heapq.heappush(self.heaps[pushIdx], num * sign)
        self.flag = 1 - self.flag

    def findMedian(self) -> float:
        return (-self.heaps[1][0] + self.heaps[-1][0]) / 2
        