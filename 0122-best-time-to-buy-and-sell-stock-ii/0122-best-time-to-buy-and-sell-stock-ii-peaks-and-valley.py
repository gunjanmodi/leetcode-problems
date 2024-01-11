class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        peak, valley, profit, i = 0, 0, 0, 0
        n = len(prices)

        while i < n:
            
            while i + 1 < n and prices[i] >= prices[i+1]:
                i += 1
            valley = prices[i]
            
            while i + 1 < n and prices[i] <= prices[i+1] :
                i += 1
            peak = prices[i]
            
            profit += (peak - valley)
            i += 1

        return profit
