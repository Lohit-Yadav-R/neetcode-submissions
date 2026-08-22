class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        queue = deque()
        for i in range(len(nums)):
            while queue and nums[queue[-1]] <= nums[i]:
                queue.pop()
            queue.append(i)
            if queue[0] < i - k + 1:
                queue.popleft()
            if k - 1 <= i:
                res.append(nums[queue[0]])

        
        return res