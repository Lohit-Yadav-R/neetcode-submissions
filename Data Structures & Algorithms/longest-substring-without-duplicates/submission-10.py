class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l = 0
        count = defaultdict(lambda : -1)
        for r in range(len(s)):
            if count[s[r]] != -1:
                l = max(count[s[r]] + 1, l)
            count[s[r]] = r
            res = max(res, r - l + 1)
        return res