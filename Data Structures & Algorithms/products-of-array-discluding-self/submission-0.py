class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero_count = 0
        productzero = 1
        for num in nums:
            if num == 0:
                zero_count += 1
                product = 0
                continue
            product *= num
            productzero *= num
        if zero_count <2:
            prodarr = [product // num if num != 0 else productzero for num in nums]
        else:
            prodarr = [0] * len(nums)
        return prodarr