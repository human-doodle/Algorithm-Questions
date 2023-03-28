'''

#fibonacci #recirsive #dp

Porblem Statement: 
 Leetcode: 70. Climbing Stairs : https://leetcode.com/problems/climbing-stairs/description/

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 

Constraints:

1 <= n <= 45


'''

class Solution:
    '''
    #recursive
    def climbStairs(self, n: int) -> int:
        # only ine way to reach goal
        if n==1:
            return 1
        #only two ways to reach goal
        elif n==2:
            return 2
        else:
            return self.climbStairs(n-1)+ self.climbStairs(n-2)
    '''
    

    #dp
    def climbStairs(self, n: int) -> int:
        answer = [0] * (n+2)
        answer[1]=1
        answer[2]=2
            
        for i in range(3,n+1):
            answer[i]=answer[i-1]+answer[i-2]
        return answer[n]
