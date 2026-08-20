class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        self.end = len(nums)
        def backtrack(temp, start, sum):
            if sum == target:
                res.append(temp[:])
                return
            if sum > target:
                return
            for i in range(start, self.end):
                temp.append(nums[i])
                backtrack(temp, i, sum + nums[i])
                temp.pop()
            

            
            

        
        backtrack([], 0, 0)

        return res