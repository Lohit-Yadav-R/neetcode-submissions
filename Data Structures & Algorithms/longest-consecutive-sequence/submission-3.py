class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        res = 0
        for num in nums:
            if num - 1 not in hashset:
                count = 1
                curr = num
                while curr + 1 in hashset:
                    count += 1
                    curr += 1 
                res = max(res, count)
        return res