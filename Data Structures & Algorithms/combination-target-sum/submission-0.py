class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        self.r = len(nums) - 1
        def backtrack(temp, l, sum):
            if sum == target:
                res.append(temp[:])
                return
            if sum > target:
                return
            while l < self.r:
                backtrack(temp[:] + [nums[l]], l, sum + nums[l])
                l += 1
            

            
            

        
        backtrack([], -1, 0)

        return res