class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        lists, listt = [0] * 26, [0] * 26 
        for i in range (len(s)):
            lists[ord(s[i]) - ord('a')] += 1 
            listt[ord(t[i]) - ord('a')] += 1
        if lists == listt:
            return True
        return False