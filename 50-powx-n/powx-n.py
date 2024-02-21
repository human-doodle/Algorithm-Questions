class Solution:
    def myPow(self, x: float, n: int) -> float:

        ans = 1
        nn = n
        if nn<0:
            nn = -1*nn
        while nn:
            if nn%2 == 1:
                ans = ans*x
                nn -= 1
            else:
                x = x * x
                nn //= 2
        if n < 0:
            ans = 1/ans
        
        return ans

        # O(logn)