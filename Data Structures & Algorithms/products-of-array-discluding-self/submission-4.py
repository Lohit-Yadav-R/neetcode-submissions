class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        preprod = [1] * len(nums)
        suffprod = [1] * len(nums)
        prefix = 1
        suffix = 1
        for i in range(len(nums)):
            preprod[i] = prefix
            prefix *= nums[i]
        for i in range(len(nums) - 1, -1, -1):
            suffprod[i] = suffix
            suffix *= nums[i]
        res = []
        for i in range(len(nums)):
            res.append(preprod[i] * suffprod[i])
        return res