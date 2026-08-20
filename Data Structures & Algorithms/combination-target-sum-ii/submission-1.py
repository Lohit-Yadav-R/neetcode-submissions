class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        self.end = len(candidates)
        def backtrack(temp, start, sum):
            if sum == target:
                res.append(temp[:])
                return
            if sum > target:
                return
            for i in range(start, self.end):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                temp.append(candidates[i])
                backtrack(temp, i + 1, sum + candidates[i])
                temp.pop()
            

            
            

        
        backtrack([], 0, 0)

        return res