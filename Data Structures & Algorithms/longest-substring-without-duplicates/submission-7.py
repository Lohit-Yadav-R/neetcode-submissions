class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashset = set()
        l, r = 0, 0
        res = 0
        length = 0
        while r < len(s):
            if s[r] in hashset:
                while s[r] in hashset:
                    hashset.remove(s[l])
                    l += 1
                    length -= 1
                    
            length += 1
            hashset.add(s[r])
            res = max(res, length)
            r += 1
        return res