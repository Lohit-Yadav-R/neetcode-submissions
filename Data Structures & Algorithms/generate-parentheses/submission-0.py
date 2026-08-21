class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        open, closeNeeded = 0, 0
        self.maxSize = 2 * n
        res = []

        def backtrack(string, open, closeNeeded, size):
            if size == self.maxSize:
                res.append(string)
                return
            
            if open < n:
                backtrack(string + '(', open + 1, closeNeeded + 1, size + 1)
            
            if closeNeeded > 0:
                backtrack(string + ')', open, closeNeeded - 1, size + 1)
        
        backtrack('', 0, 0, 0)

        return res