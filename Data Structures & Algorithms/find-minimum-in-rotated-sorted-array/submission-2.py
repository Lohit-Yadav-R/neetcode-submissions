class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            if l + 1 == r or l == r:
                return min(nums[l],nums[r])
            m = l + ((r - l) // 2)
            if nums[l] <= nums[m] and nums[m] <= nums[r]:
                return nums[l]
            if nums[l] <= nums[m]:
                l = m
            elif nums[m] <= nums[r]:
                r = m