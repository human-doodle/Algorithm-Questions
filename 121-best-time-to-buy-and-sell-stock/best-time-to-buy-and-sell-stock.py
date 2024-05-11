class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        prev = float('inf')
        for price in prices:
            if prev>price:
                prev = min(prev, price)
                continue
            maxprofit = max(maxprofit, price-prev)
        return maxprofit


'''
O(n) O(1)
maxprofit = 0
cp = float('inf')
[7,1,5,3,6,4]
            p
 cp = min(cp, i)   
Output: 5
'''