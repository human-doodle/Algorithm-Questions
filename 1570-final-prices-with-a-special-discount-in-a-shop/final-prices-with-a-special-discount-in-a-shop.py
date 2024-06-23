class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        res = prices[:]

        stack = []
        for i, price in enumerate(prices):
            while stack and prices[stack[-1]]>=price:
                idx = stack.pop()
                res[idx] = (prices[idx]-price)
            stack.append(i)
        
        return res
# [8,4,6,2,3]
#        ^
# [2, 3]
# [4,2,4,2,3]