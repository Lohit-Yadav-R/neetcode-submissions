class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = {}
        for num in nums:
            count_map[num] = 1 + count_map.get(num, 0)
        count_map = dict(sorted(count_map.items(), key = lambda item : item[1], reverse = True))
        return list(count_map.keys())[:k]