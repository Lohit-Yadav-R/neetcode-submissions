class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set()
        subset = []
        n = len(nums)
        def backtrack(depth):
            if depth == n:
                res.add(tuple(sorted(subset)))
                return
            
            backtrack(depth + 1)
            subset.append(nums[depth])
            backtrack(depth + 1)
            subset.pop()
        
        backtrack(0)
        
        return [list(_) for _ in res]