class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        
        
        largest = 0
        for pile in piles:
            largest = max(largest, pile)
        l = 1
        r = largest
        k = largest
        while l <= r:
            m = l + ((r - l) // 2)
            if self.isValid(piles, h, m):
                k = min(k, m)
                r = m - 1
            else:
                l = m + 1
        return k


    def isValid(self, piles: List[int], h: int, k: int):
            time = 0
            for pile in piles:
                time += -(pile // -k)
            if time <= h:
                return True
            return False