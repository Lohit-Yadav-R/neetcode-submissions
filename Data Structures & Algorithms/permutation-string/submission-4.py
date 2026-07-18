class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        count1 = [0] * 26
        matches = 0
        for c in s1:
            count1[ord(c) - ord('a')] += 1
        winlen = len(s1)
        wincount = [0] * 26
        l = 0
        for i in range(winlen):
            wincount[ord(s2[i]) - ord('a')] += 1
        for i in range(26):
            if count1[i] == wincount[i]:
                matches += 1
        for r in range(winlen, len(s2)):
            if matches == 26:
                return True
            if wincount[ord(s2[l]) - ord('a')] == count1[ord(s2[l]) - ord('a')]:
                matches -= 1
            wincount[ord(s2[l]) - ord('a')] -= 1
            if wincount[ord(s2[l]) - ord('a')] == count1[ord(s2[l]) - ord('a')]:
                matches += 1
            l += 1
            if wincount[ord(s2[r]) - ord('a')] == count1[ord(s2[r]) - ord('a')]:
                matches -= 1
            wincount[ord(s2[r]) - ord('a')] += 1
            if wincount[ord(s2[r]) - ord('a')] == count1[ord(s2[r]) - ord('a')]:
                matches += 1
        return matches == 26
