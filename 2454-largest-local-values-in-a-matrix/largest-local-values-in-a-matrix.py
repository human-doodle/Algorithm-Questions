class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        rows, cols = len(grid)-2, len(grid[0])-2

        res = [[-1 for _ in range(rows)] for _ in range(cols)]

        for i in range(rows):
            for j in range(cols):
                grid_max = -1
                for k in range(3):
                    for l in range(3):
                        grid_max = max(grid_max, grid[k+i][l+j])
                res[i][j] = grid_max
        
        return res


'''
Input: grid =  [[1,1,1,1,1],
                [1,1,1,1,1],    
                [1,1,2,1,1],
                [1,1,1,1,1],
                [1,1,1,1,1]]
Output: [[2,2,2],[2,2,2],[2,2,2]]
'''