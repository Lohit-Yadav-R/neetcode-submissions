class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[nums[0]]
        while nums[slow] != nums[fast]:
            slow = nums[slow]
            fast = nums[nums[fast]]
        
        slow2 = 0
        while nums[slow2] != nums[slow]:
            slow2 = nums[slow2]
            slow = nums[slow]
        return nums[slow]