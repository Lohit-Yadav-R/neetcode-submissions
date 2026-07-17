class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        left = 0
        right = left + 1
        while right < len(prices):
            profit = prices[right] - prices[left]
            if profit < 0:
                left = right
                right += 1
            else:
                res = max(res, profit)
                right += 1
        return res