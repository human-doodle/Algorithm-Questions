class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0] * n

        for i in range(n):
            max_val = 0
            for j in range(1, min(k, i + 1) + 1):
                max_val = max(max_val, arr[i - j + 1])
                dp[i] = max(dp[i], (dp[i - j] if i - j >= 0 else 0) + max_val * j)

        return dp[-1]