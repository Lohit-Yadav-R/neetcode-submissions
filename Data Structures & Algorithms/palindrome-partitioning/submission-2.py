class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        possList = []
        self.n = len(s)
        def backtrack(idx):
            if idx == self.n:
                res.append(possList[:])
                return
            
            substr = ''
            for i in range(idx, self.n):
                substr = substr + s[i]
                if isPalindrome(substr):
                    possList.append(substr)
                    backtrack(i + 1)
                    possList.pop()
        
        def isPalindrome(substr):
            l = 0
            r = len(substr) - 1
            while l < r:
                if substr[l] != substr[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        backtrack(0)

        return res
