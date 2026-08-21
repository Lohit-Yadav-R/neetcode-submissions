class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        comb = []
        self.end = len(candidates)

        def backtrack(start, sum):
            if sum == target:
                res.append(comb.copy())
                return
            if sum > target:
                return
            
            for i in range(start, self.end):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                comb.append(candidates[i])
                backtrack(i + 1, sum + candidates[i])
                comb.pop()

        backtrack(0, 0)

        return res