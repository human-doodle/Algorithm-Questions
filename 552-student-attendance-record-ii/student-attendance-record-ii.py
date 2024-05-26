class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10**9 + 7
        dp = [[[0] * 3 for _ in range(2)] for _ in range(n + 1)]
        dp[0][0][0] = 1  # Base case
        
        for i in range(1, n + 1):
            for j in range(2):  # 0 or 1 'A's
                for k in range(3):  # 0 to 2 consecutive 'L's
                    # Add 'P'
                    dp[i][j][0] = (dp[i][j][0] + dp[i-1][j][k]) % MOD
                    # Add 'A'
                    if j == 0:
                        dp[i][1][0] = (dp[i][1][0] + dp[i-1][j][k]) % MOD
                    # Add 'L'
                    if k < 2:
                        dp[i][j][k+1] = (dp[i][j][k+1] + dp[i-1][j][k]) % MOD
        
        # Sum all valid dp[n][j][k]
        result = 0
        for j in range(2):
            for k in range(3):
                result = (result + dp[n][j][k]) % MOD
        
        return result
