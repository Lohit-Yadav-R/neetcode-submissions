class Solution:
    def minWindow(self, s: str, t: str) -> str:
        win = {}
        countt = {}
        l = 0
        res = ''
        resLen = float('Inf')
        match = 0
        for c in t:
            countt[c] = countt.get(c, 0) + 1
        need = len(countt)
        for r in range(len(s)):
            win[s[r]] = win.get(s[r], 0) + 1
            if s[r] in countt and win[s[r]] == countt[s[r]]:
                match += 1
            while match == need:
                if r - l + 1 < resLen:
                    res = s[l : r + 1]
                    resLen = r - l + 1
                if s[l] in countt and win[s[l]] == countt[s[l]]:
                    match -= 1
                win[s[l]] -= 1
                l += 1
        return res