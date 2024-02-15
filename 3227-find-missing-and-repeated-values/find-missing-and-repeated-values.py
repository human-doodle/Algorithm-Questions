class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        
        n = len(grid)

        # MAthematical : O(n^2) TC O(1) SC

        N = n**2 # N: total consecutive natural numbers
        sum_N = N*(N+1)//2 # sum of N natural numbers
        sum_N2 = N*(N+1)*(2*N+1)//6 # sum of squares of first N numbers

        sum_grid, sum_grid2 = 0,0
        #calculate sum adn sum of square of elements of grid
        for i in range(n):
            for j in range(n):
                sum_grid+=grid[i][j]
                sum_grid2 += grid[i][j]**2
        
        AminusB = sum_grid - sum_N # A-B
        A2minusB2 = sum_grid2 - sum_N2 #A^2-B^2
        AplusB = (A2minusB2//AminusB) #A+B
        A = (AplusB + AminusB)//2
        B = (AplusB - A)

        return [A,B]





        # brute force
        
        # n = len(grid)

        # check = [0 for _ in range(0, n**2)]
        # a, b = -1, -1

        # for i in range(n):
        #     for j in range(n):
        #         idx = grid[i][j] - 1
        #         check[idx]+=1

        # for i in range(n**2):
        #     if check[i] == 0:
        #         b = i+1
        #     elif check[i] == 2:
        #         a = i+1
            
        # return [a, b]

# O(n^2) TC O(n^2) sc