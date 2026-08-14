class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        counts = [0] * 26
        wincount = [0] * 26
        match = 0
        l = 0
        r = len(s1) - 1
        for c in s1:
            counts[ord(c) - ord('a')] += 1
        for i in range(len(s1)):
            wincount[ord(s2[i]) - ord('a')] += 1
        for i in range(26):
            if wincount[i] == counts[i]:
                match += 1
        if match == 26:
                return True
        while r < len(s2) - 1:
            r += 1
            r_idx = ord(s2[r]) - ord('a')
            wincount[r_idx] += 1
            if wincount[r_idx] - 1 == counts[r_idx]:
                match -= 1
            if wincount[r_idx] == counts[r_idx]:
                match += 1
            l_idx = ord(s2[l]) - ord('a')
            wincount[l_idx] -= 1
            if wincount[l_idx] + 1 == counts[l_idx]:
                match -= 1
            if wincount[l_idx] == counts[l_idx]:
                match += 1
            l += 1
            if match == 26: return True
        return False