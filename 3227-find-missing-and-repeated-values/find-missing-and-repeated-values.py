class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
       
        # brute force
        
        n = len(grid)

        check = [0 for _ in range(0, n**2)]
        a, b = -1, -1

        for i in range(n):
            for j in range(n):
                idx = grid[i][j] - 1
                check[idx]+=1

        for i in range(n**2):
            if check[i] == 0:
                b = i+1
            elif check[i] == 2:
                a = i+1
            
        return [a, b]
# O(n^2) TC O(n^2) sc