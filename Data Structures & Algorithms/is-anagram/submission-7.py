class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        counts = [0]*26
        countt = [0]*26
        for c in s:
            counts[ord(c) - ord('a')] += 1
        for c in t:
            countt[ord(c) - ord('a')] += 1
        return counts == countt