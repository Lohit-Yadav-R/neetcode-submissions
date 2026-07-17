class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        string = ''
        length = 1
        for c in s:
            if c in string:
                length = max(length, len(string))
                string = string.partition(c)[2] + c
            else:
                string += c
        if c in string:
                length = max(length, len(string))
                string = c
        return length