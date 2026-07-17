class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count_map = [0] * 26
            for c in s:
                count_map[ord(c) - ord('a')] += 1
            res[tuple(count_map)].append(s)
        return list(res.values())