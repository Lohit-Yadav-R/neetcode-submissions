class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        perm = []
        visited = set()

        def backtrack():
            if len(perm) == len(nums):
                res.append(perm[:])
                return
            
            for num in nums:
                if num not in visited:
                    visited.add(num)
                    perm.append(num)

                    backtrack()

                    visited.remove(num)
                    perm.remove(num)
        
        backtrack()
        return res