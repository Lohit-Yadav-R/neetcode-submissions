class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k <= 0:
            return []
        
        res = []
        dq = deque()
        for i, num in enumerate(nums):
            while dq and nums[dq[-1]] <= num:
                dq.pop()

            dq.append(i)

            if dq[0] < i - k + 1:
                dq.popleft()
            
            if k - 1 <= i:
                res.append(nums[dq[0]])
        return res