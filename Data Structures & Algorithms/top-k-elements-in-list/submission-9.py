class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        freq = [[] for _ in range(len(nums) + 1)]
        hashmap = {}
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
        for num, count in hashmap.items():
            freq[count].append(num)
        for i in range(len(freq) - 1, -1, -1):
            while freq[i]:
                res.append(freq[i].pop())
                if len(res) == k:
                    return res