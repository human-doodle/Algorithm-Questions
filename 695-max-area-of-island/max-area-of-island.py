class Solution:
    def exploreIsland(self, grid, r, c, visited):
        rowInbound = r>=0 and r<len(grid)
        colInbound = c>=0 and c<len(grid[0])
        if not rowInbound or not colInbound: return 0

        if grid[r][c] == 0: return 0

        if (r, c) in visited: return 0

        visited.add((r,c))

        size = 1
        size += self.exploreIsland( grid, r-1, c, visited)
        size += self.exploreIsland( grid, r+1, c, visited)
        size += self.exploreIsland( grid, r, c-1, visited)
        size += self.exploreIsland(grid, r, c+1, visited)

        return size

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maximum_area = -float('inf')
        visited = set()

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                maximum_area = max(maximum_area, self.exploreIsland(grid, r, c, visited))
        return maximum_area