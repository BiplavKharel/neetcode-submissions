class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_profit = 0
        min_ind = 0
        for i in range(len(prices)):
            
            max_profit = max(max_profit,prices[i] - prices[min_ind])

            if prices[min_ind] > prices[i]:
                min_ind = i
        return max_profit

