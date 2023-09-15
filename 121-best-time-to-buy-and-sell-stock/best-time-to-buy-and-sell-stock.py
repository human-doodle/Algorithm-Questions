class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minbuy, maxp = float('inf'), 0
        
        for i in range(len(prices)):
                if prices[i]<minbuy:
                    minbuy = prices[i]
                    continue
                profit =  prices[i] - minbuy
                maxp = max(maxp, profit)
        return maxp
            
# TC: O(n)
# SC : O(1)
        