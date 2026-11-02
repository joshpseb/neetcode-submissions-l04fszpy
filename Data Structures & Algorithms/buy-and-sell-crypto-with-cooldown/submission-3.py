class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # bottom up dp optimized
        # only need next day sell, next day buy, and two days later buy 
        
        n = len(prices)

        #dp = [[0] * 2 for _ in range(n + 2)]
        nextSell = 0
        nextBuy = 0
        nextnextBuy = 0
        

        for i in range(n - 1, -1, -1):
            #dp[i][0] = max(-prices[i] + dp[i + 1][1], dp[i + 1][0])
            #dp[i][1] = max(prices[i] + dp[i + 2][0], dp[i + 1][1])
            currBuy = max(-prices[i] + nextSell, nextBuy)
            currSell = max(prices[i] + nextnextBuy, nextSell)
            # currBuy becomes next, next become nextnext
            # currSell becomes next
            nextnextBuy = nextBuy
            nextBuy = currBuy
            nextSell = currSell
        
        return currBuy