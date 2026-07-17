class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        res = 0
        while left < right:
            shorter = min(heights[left], heights[right])
            res = max(res, (shorter * (right - left)))
            if shorter == heights[left]:
                left += 1
            else:
                right -= 1
        return res