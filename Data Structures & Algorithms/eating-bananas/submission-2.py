class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        mid = 0
        while l <= r:
            mid = l + ((r - l) // 2)
            if self.isvalid(piles, h, mid):
                r = mid - 1
                res = mid
            else:
                l = mid + 1
        return res
    def isvalid(self, piles, h, k):
        time = 0
        for num in piles:
            time += -num // k
        if -time <= h:
            return True
        return False