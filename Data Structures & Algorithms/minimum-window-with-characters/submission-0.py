class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ''
        res = s + 'a'
        countt, wincount = {}, {}
        l = 0
        for c in t:
            countt[c] = 1 + countt.get(c, 0)
        match = 0
        for r in range(len(s)):
            if s[r] in countt:
                wincount[s[r]] = 1 + wincount.get(s[r], 0)
                if wincount[s[r]] == countt[s[r]]:
                    match += 1
            while match == len(countt):
                if len(res) > r - l + 1:
                    res = s[l: r + 1]
                if s[l] in wincount:
                    wincount[s[l]] -= 1
                    if wincount[s[l]] < countt[s[l]]:
                        match -= 1
                l += 1
        if res != s + 'a':
            return res
        return ''









