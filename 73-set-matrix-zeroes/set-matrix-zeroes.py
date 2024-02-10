class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])

        rowl = set()
        coll = set()

        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    rowl.add(i)
                    coll.add(j)
        
        for i in range(row):
            for j in range(col):
                if i in rowl or j in coll:
                    matrix[i][j] = 0

