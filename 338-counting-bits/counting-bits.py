class Solution:
    def countBits(self, n: int) -> List[int]:

        # dp O(n)
        dp = [0]*(n+1)

        for i in range(1, n+1):
            dp[i] = dp[i >> 1] + (i & 1)
        
        return dp

        # # O(nlogn) because n is represented by logn bits in binary
        # def count_ones(num):
        #     count = 0
        #     while num > 0:
        #         count += num & 1
        #         num >>= 1
        #     return count

        # result = []
        # for i in range(n + 1):
        #     result.append(count_ones(i))
        # return result

        