class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price, max_profit = prices[0], 0

        for i in range(1, len(prices)):
            if prices[i] < buy_price:
                buy_price = prices[i]
            max_profit = max(max_profit, prices[i] - buy_price)
            
        return max_profit
            
        