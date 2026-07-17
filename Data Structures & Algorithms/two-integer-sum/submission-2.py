class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_hashmap = {} # val : index
        for i, num in enumerate(nums):
            complement = target - num
            if complement in prev_hashmap:
                return [prev_hashmap[complement], i]
            prev_hashmap[num] = i
        return