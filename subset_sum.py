# referred: https://www.youtube.com/watch?v=s6FhG--P7z0

def subset_sum(nums: list[int], sum: int) -> bool:
    n = len(nums)
    # we'll make a dp array len(nums) X (sum+1) matrix
    # initialize the dp array with first row as false
    dp = [[False for _ in range(sum+1)] for _ in range(n+1)]
    
    # inintialize value of true for first column, where 
    # sum = 0( it can be foemd with a empty aray, 
    # so should return true)
    for i in range(n+1):
        dp[i][0] = True
        
    # we check for each number in the array if a particular sum be 
    # attained using previously encountered elements of the array
    # row iteration for eah elemnt of the array
    for i in range(1, n+1):
        # column interation for all teh sums upto sum
        for j in range(1, sum+1):
            # if the i-1th element of the array is less than the current sum j, 
            # assign the value of the prvious element dp[i-1][j] or dp[i-1][j-nums[i-1]]
            if j >= nums[i-1]:
                dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
            else:
                # else, assign it as dp[i-1][j]
                dp[i][j] = dp[i-1][j]
    
    return dp[n][sum]
