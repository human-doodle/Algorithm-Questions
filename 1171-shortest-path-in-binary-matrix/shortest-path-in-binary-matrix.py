class Solution:
    def check_inbounds(self,grid, r, c):
        return r>=0 and r<len(grid) and c>=0 and c<len(grid[0])
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        visited = set()
        q = deque([(0,0,1)])
        directions = [[-1, 0],[0,-1],
                     [1, 0],[0, 1],
                     [-1, -1],[1, 1],
                     [-1, 1],[1, -1]]
        while q:
            r, c, path = q.popleft()
            if not self.check_inbounds(grid, r,c) or grid[r][c] == 1 or (r,c) in visited:
                continue
            if (r,c) == (len(grid)-1, len(grid[0])-1):
                return path
            visited.add((r,c))
            for offset_r, offset_c in directions:
                q.append((r+offset_r,c+offset_c,path+1))
        return -1

        