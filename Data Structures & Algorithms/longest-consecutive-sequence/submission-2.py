class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        res = 0
        for i in range(len(nums)):
            if nums[i] - 1 not in num_set:
                seq_num = nums[i]
                seq_len = 1
                while (seq_num + 1) in num_set:
                    seq_num += 1
                    seq_len += 1
                res = max(res, seq_len)
        return res