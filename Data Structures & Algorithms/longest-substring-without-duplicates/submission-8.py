class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l = 0
        count = defaultdict(lambda : -1)
        for r in range(len(s)):
            count[s[r]] += 1
            while count[s[r]] > 0:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res