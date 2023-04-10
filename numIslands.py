"""

#graph #dfs

link: https://leetcode.com/problems/number-of-islands/description/

200. Number of Islands
Medium

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

"""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """ 
        Logic: we do dfs on each cell with value '1'. During dfs, we mark all connected 1's as visited and count each traversal as 1 island.
        This is because for each traversal, we exit the function if we find water'0' or overflowing bounds. 
        
        """

        # define a dfs function taking the indexes of the grid as an input and performing dfs on the connected cells
        def _dfs(x,y):
            # return if the cell is water/visited/out of bounds 
            if(x<0 or x>=len(grid) or y<0 or y>=len(grid[0]) or grid[x][y] == '0' or  grid[x][y] == 'visited'):
                return
            # else mark visited
            grid[x][y] = 'visited'
            # perform dfs on the neighboring connected cells
            _dfs(x-1,y)
            _dfs(x+1,y)
            _dfs(x,y-1)
            _dfs(x,y+1)

        num_islands = 0
        grid_rows = len(grid)
        grid_col = len(grid[0])

        # check for each cell
        for i in range(grid_rows):
            for j in range(grid_col):
                # for every dfs of cell with valie '1', we increament num_islands
                if grid[i][j] == '1':
                    _dfs(i,j)
                    num_islands += 1
                
        return num_islands

            


