class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set()
        res = 0
        for i in range(len(nums)):
            hashset.add(nums[i])
        for num in hashset:
            if num - 1 in hashset:
                continue
            cur = num
            cur_res = 0
            while cur in hashset:
                cur_res += 1
                cur += 1
            res = max(res, cur_res)
        return res
            