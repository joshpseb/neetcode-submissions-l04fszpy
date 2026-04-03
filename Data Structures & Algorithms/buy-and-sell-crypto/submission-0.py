class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minPrice = float('inf')
        for i in range(len(prices)):
            profit = prices[i] - minPrice
            minPrice = min(minPrice, prices[i])
            maxProfit = max(profit, maxProfit)
        return maxProfit