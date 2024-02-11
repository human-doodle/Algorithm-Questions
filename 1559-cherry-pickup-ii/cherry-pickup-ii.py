class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        
        # dp[row][col1][col2] represents the maximum cherries collected starting from (row, col1) and (row, col2)
        dp = [[[-1] * cols for _ in range(cols)] for _ in range(rows)]
        
        def dfs(row, col1, col2):
            if row == rows:
                return 0
            
            if dp[row][col1][col2] != -1:
                return dp[row][col1][col2]
            
            cherries = grid[row][col1] if col1 == col2 else grid[row][col1] + grid[row][col2]
            max_cherries = 0
            
            for move1 in [-1, 0, 1]:
                for move2 in [-1, 0, 1]:
                    new_col1, new_col2 = col1 + move1, col2 + move2
                    
                    if 0 <= new_col1 < cols and 0 <= new_col2 < cols:
                        max_cherries = max(max_cherries, cherries + dfs(row + 1, new_col1, new_col2))
            
            dp[row][col1][col2] = max_cherries
            return max_cherries
        
        return dfs(0, 0, cols - 1)
      