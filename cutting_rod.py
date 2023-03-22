# refered : # https://www.youtube.com/watch?v=IRwVmTmN6go

def cutting_rod(prices, n):
    
    dp = [[0] * (n+1) for _ in range(len(prices))]
    
    for i in range(len(prices)):
        dp[i][0] = 0

    for j in range(n+1):
        dp[0][j] = prices[0]*j

    for i in range(1,len(prices)):
        for j in range(1, n+1):
            if i+1>j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(prices[i] + dp[i][j-i-1], dp[i-1][j])
  
    return dp[len(prices)-1][n]    
