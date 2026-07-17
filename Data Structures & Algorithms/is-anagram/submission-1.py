class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counts,countt={},{}
        for c in s:
            counts[c] = 1 + counts.get(c, 0)
        for c in t:
            countt[c] = 1 + countt.get(c, 0)
        for c in counts:
            if counts[c] != countt.get(c, 0):
                return False
        return True