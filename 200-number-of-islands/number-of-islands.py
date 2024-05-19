class Solution:
    def dfs(self, grid, r, c, visited):
        row_inbound = r>=0 and r<len(grid)
        col_inbound = c>=0 and c<len(grid[0])
        if not row_inbound or not col_inbound: return False

        if grid[r][c] == '0': return False

        if (r,c) in visited: return False

        visited.add((r,c))

        self.dfs(grid, r-1, c, visited)
        self.dfs(grid, r+1, c, visited)
        self.dfs(grid, r, c-1, visited)
        self.dfs(grid, r, c+1, visited)

        return True


    def numIslands(self, grid: List[List[str]]) -> int:
        row, col = len(grid), len(grid[0])
        visited = set()
        count = 0
        for r in range(row):
            for c in range(col):
                if self.dfs(grid, r, c, visited):
                    count+=1
        return count






        # if not grid:
        #     return 0
        
        # rows, cols = len(grid), len(grid[0])
        # visit = set()
        # islands = 0
        
        # def bfs(r,c):
        #     q = collections.deque()
        #     visit.add((r, c))
        #     q.append((r, c))

        #     while q:
        #         row, col = q.popleft()
        #         directions = [[1,0], [-1, 0], [0,1], [0,-1]]

        #         for dr, dc in directions:
        #             r, c = row + dr, col + dc
        #             if (r in range(rows) and 
        #                 c in range(cols) and 
        #                 grid[r][c] == "1" and
        #                 (r, c) not in visit):
        #                 q.append((r, c))
        #                 visit.add((r, c))

        # for r in range(rows):
        #     for c in range(cols):
        #         if grid[r][c] == "1" and (r,c) not in visit:
        #             bfs(r,c)
        #             islands+=1
        # return islands