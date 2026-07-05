class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profits=set()
        
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                if prices[i]<prices[j]:
                    profit=prices[j]-prices[i]
                    profits.add(profit)
                    
        if profits:
            return max(profits)
        else:
            return 0

