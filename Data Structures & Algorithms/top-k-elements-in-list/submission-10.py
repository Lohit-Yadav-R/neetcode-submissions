class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for _ in range(len(nums) + 1)]
        hashmap = defaultdict(int)
        res = []
        for num in nums:
            hashmap[num] += 1
        
        for key, val in hashmap.items():
            freq[val].append(key)
        
        for i in range(len(freq) - 1, -1, -1):
            while freq[i]:
                res.append(freq[i].pop())
                if len(res) == k:
                    return res