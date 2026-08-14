class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0] * len(nums)
        suffix = [0] * len(nums)
        res = [0] * len(nums)
        pre, suf, = 1, 1
        for i in range(len(nums)):
            prefix[i] = pre
            pre = pre * nums[i]
        for i in range(len(nums) - 1, -1, -1):
            suffix[i] = suf
            suf = suf * nums[i]
        for i in range(len(nums)):
            res[i] = prefix[i] * suffix[i]
        return res