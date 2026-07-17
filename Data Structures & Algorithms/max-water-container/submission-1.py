class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len (heights) -1
        volume = 0
        while left < right:
            shorter = min(heights[left], heights[right])
            volume = max (volume, ( shorter * (right - left)))
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
        return volume

