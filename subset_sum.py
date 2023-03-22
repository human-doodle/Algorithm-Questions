# referred: https://www.youtube.com/watch?v=s6FhG--P7z0

def subset_sum(nums: list[int], sum: int) -> bool:
    n = len(nums)
    dp = [[False for _ in range(sum+1)] for _ in range(n+1)]
    
    for i in range(n+1):
        dp[i][0] = True
        
    for i in range(1, n+1):
        for j in range(1, sum+1):
            if j >= nums[i-1]:
                dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
            else:
                dp[i][j] = dp[i-1][j]
    
    return dp[n][sum]
