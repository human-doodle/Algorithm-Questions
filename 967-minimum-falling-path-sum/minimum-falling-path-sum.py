class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        dp = matrix
        for i in range(1, rows):
            for j in range(cols):
                # Calculate the minimum sum for each element in the current row
                dp[i][j] = matrix[i][j] + min(dp[i - 1][max(0, j - 1):min(cols, j + 2)])

        # The answer is the minimum sum in the last row
        return min(dp[-1])
        