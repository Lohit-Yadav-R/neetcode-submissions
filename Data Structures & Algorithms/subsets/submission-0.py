class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        def backtracking(temp, depth):
            if depth == n:
                res.append(temp[:])
                return
            
            backtracking(temp[:], depth + 1)
            temp.append(nums[depth])
            backtracking(temp[:], depth + 1)

        backtracking([], 0)
        return res