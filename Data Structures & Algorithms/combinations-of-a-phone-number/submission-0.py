class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digit_to_char = {
    '2': "abc",
    '3': "def",
    '4': "ghi",
    '5': "jkl",
    '6': "mno",
    '7': "pqrs",
    '8': "tuv",
    '9': "wxyz"
}
        self.n = len(digits)
        def backtrack(comb, idx):
            if idx == self.n:
                if comb:
                    res.append(comb)
                return
            
            for c in digit_to_char[digits[idx]]:
                comb = comb + c
                backtrack(comb, idx + 1)
                comb = comb[ : -1]
        
        backtrack('', 0)
        return res