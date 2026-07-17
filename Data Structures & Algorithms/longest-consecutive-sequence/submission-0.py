class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        NumSet = set(nums)
        longest = 0
        for num in NumSet:
            if (num -1 ) not in NumSet:
                length =1

                while (num +1) in NumSet:
                    length +=1
                    num += 1
                longest = max(longest, length)
        return longest