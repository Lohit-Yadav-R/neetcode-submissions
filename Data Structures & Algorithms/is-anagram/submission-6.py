class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counts = {}
        countt = {}

        for i in range(len(s)):
            counts[s[i]] = counts.get(s[i], 0) + 1
            countt[t[i]] = countt.get(t[i], 0) + 1
        
        return counts == countt