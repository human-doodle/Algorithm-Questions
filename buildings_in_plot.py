'''
Problem Statement:

A real estate developer wants to buy plot of land and construct residential buildings to sell them for profit. 
The plot of land he can buy is available in the shape of 3 x n and the residential building he wants to construct 
has a shape of 2 x 1. He wants to find the number of ways he can arrage these buildings either vertically or horizontally.

Note: Return 0 if the plot of land can not be completely covered by the buildings. 


'''

def no_of_ways(n: int):
# This function takes an integer n as input and returns the number of ways to arrange  a set of tiles of size 2x1 in a grid of size 3xn.
   
    # If n is an oddd number, theree is no way to aarrange the tiles, so0 return 0.
    if n % 2 == 1:
        return 0
    
    # Create a list dp of siize n+1 with the initial valeues [1, 0, 3] and n-2 zeroes where dp[i]  storess the number of wayts to arrange buildings.
    # when n = 0, the no_odf ways is 1, for 1, it's 0, and for 2 it's 3 andso on..
    dp = [1, 0, 3] + [0] * (n-2)
    
    # Calculate the number of ways to arrange the buildings for each even i from 4 to n, because odd  i's will be 0 always
    # We use the formula 4 * dp[i-2] - dp[i-4] to calculate dp[i] 
    # 3 x i is equal to 4 times the number of ways to arrange the buildings in a plot of size 3 x i-2, 
    # minus the number of "bad" arrangements that cannot be extended to a valid arrangement in a plot of size 3 x i
    for i in range(4, n+1, 2):
        dp[i] = 4 * dp[i-2] - dp[i-4]
    
    # Return dp[n], which is the number of ways to arrange the tiles in a grid of size 2xn.
    return dp[n]

