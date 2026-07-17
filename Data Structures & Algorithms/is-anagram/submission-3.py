class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counts, countt = [0] * 26, [0] * 26
        for i in range(len(s)):
            counts[ord(s[i]) - ord('a')] += 1
            countt[ord(t[i]) - ord('a')] += 1
        return counts == countt
        