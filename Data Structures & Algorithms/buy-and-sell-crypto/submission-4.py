class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        if len(prices) < 2:
            return profit
        l = 0
        r = 1
        while r < len(prices):
            if prices[r] < prices[l]:
                l = r
                r += 1
            if r < len(prices):
                profit = max(profit, prices[r] - prices[l])
            r += 1
        return profit