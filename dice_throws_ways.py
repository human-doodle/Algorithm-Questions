'''
PROBLEM STATEMENT: 
Given n dice each with m faces, numbered from 1 to m, find the number of ways to get sum X. X is the summation of values
on each face when all the dice are thrown.
'''

def dice_throws_ways(m, n, x):
    # m: number of faces in dice
    # n: number of dice
    # x: target sum to achieve

    
    dp = [[0]*(x+1) for _ in range(n+1)]

    for face in range(1, m+1):
        if face <= x:
            dp[1][face] = 1

    for i in range(2, n+1):
        for current_sum in range(1, x+1):
            for face in range(1, m+1):
                if face < current_sum:
                    dp[i][current_sum] += dp[i-1][current_sum - face]


    number_of_ways = dp[n][x]
    return number_of_ways
