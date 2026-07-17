class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_arr = [0] * (len(nums))
        suffix_arr = [0] * (len(nums))
        prefix = 1
        suffix = 1
        for i in range (len(nums)):
            prefix_arr[i] = prefix
            prefix *= nums[i]
        for i in range (len(nums) - 1, -1, -1):
            suffix_arr[i] = suffix
            suffix *= nums[i]
        res = []
        for i in range(len(nums)):
            res.append(prefix_arr[i] * suffix_arr[i])
        return res