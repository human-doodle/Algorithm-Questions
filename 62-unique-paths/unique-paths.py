class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def countPaths(dp, i:int, j:int, m:int, n:int):
            if i == n-1 and j == m-1: return 1
            if i >= n or j >= m: return 0
            if dp[i][j]!=-1: return dp[i][j]
            else: 
                dp[i][j] = countPaths(dp, i+1, j, m, n) + countPaths(dp, i, j+1, m, n)
                return dp[i][j]
        dp = [[-1 for _ in range(m)] for _ in range(n)]
        return countPaths(dp, 0, 0, m, n)

    # O(n*n) O(n*n)
        