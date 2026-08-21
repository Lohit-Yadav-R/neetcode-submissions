class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        subset = []
        self.n = len(nums)
        def backtrack(i):
            if i == self.n:
                res.append(subset[:])
                return
            
            subset.append(nums[i])
            backtrack(i + 1)
            subset.pop()
            while i + 1 < self.n and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1)
        
        backtrack(0)

        return res