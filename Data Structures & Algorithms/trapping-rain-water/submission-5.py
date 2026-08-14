class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        l = 0
        r = len(height) - 1
        maxl = height[0]
        maxr = height[-1]
        while l < r:
            if height[l] < height[r]:
                l += 1
                maxl = max(maxl, height[l])
                res += (maxl - height[l])
            else:
                r -= 1
                maxr = max(maxr, height[r])
                res += (maxr - height[r])
        return res