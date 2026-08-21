class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        comb = []
        self.end = len(nums)

        def backtrack(start, sum):
            if sum == target:
                res.append(comb.copy())
                return
            if sum > target:
                return
            
            for i in range(start, self.end):
                comb.append(nums[i])
                backtrack(i, sum + nums[i])
                comb.pop()
        
        backtrack(0, 0)
        return res