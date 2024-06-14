class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        return self._minPathSum(grid, 0, 0, {})

    def _minPathSum(self, grid, row, col, memo):
        if (row, col) in memo:
            return memo[(row, col)]
        if row == len(grid)-1 and col == len(grid[0]) - 1:
            return grid[row][col]
        if not self.is_inbounds(grid, row, col):
            return float('inf')
        
        down_path = grid[row][col] + self._minPathSum(grid, row+1, col, memo)
        right_path = grid[row][col] + self._minPathSum(grid, row, col+1, memo)

        memo[(row, col)] = min(down_path, right_path)
        return memo[(row, col)]

    def is_inbounds(self, grid, row, col):
        return row>=0 and col>=0 and row< len(grid) and col < len(grid[0])

        