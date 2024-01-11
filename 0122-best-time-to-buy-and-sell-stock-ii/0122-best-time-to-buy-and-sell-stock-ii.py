class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        
        def helper(i, holding):
            if i == len(prices):
                return 0
            
            key = (i, holding)
            if key in memo:
                return memo[key]
            
            if holding == 1:
                memo[key] = max(prices[i] + helper(i+1, 0), helper(i+1, holding))
            
            if holding == 0:
                memo[key] = max(-prices[i] + helper(i+1, 1), helper(i+1, holding))
            
            return memo[key]

        return helper(0, 0)
