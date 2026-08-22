class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxheap = []
        res = []
        for r in range(len(nums)):
            heapq.heappush(maxheap, (-nums[r], r))
            if r >= k - 1:
                while maxheap[0][1] <= r - k:
                    heapq.heappop(maxheap)
                res.append(-maxheap[0][0])
        return res