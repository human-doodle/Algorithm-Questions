class Solution:
    def climbStairs(self, n: int) -> int:
        # rec sulution
        # def rec(num):
        #     if num == 1 or num == 2:
        #         return num
        #     return rec(num-1) + rec (num-2)
        # return rec(n)
        # dp solution
        if n<=2:
            return n
        dp = [0 for _ in range(n)]
        dp[0], dp[1] = 1,2
        for i in range(2, n):
            dp[i] = dp[i-1]+dp[i-2]
        return dp[n-1]

        
        
        