class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        maxProfit = []
        minCapital = [(c, p) for c, p in zip(capital, profits)]
        heapq.heapify(minCapital)

        for i in range(k):
            while minCapital and minCapital[0][0]<=w:
                c, p = heapq.heappop(minCapital)
                heapq.heappush(maxProfit, -p)
            if not maxProfit:
                break
            w += - heapq.heappop(maxProfit)
        
        return w