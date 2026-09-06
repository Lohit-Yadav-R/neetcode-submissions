class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0
        for r in range(len(heights)):
            l = r
            while stack and stack[-1][1] >= heights[r]:
                l, h = stack.pop()
                b = r - l
                area = b * h
                res = max(res, area)
            stack.append((l, heights[r]))
        
        r = len(heights)
        while stack:
            l, h = stack.pop()
            b = r - l
            area = b * h
            res = max(res, area)
        
        return res