class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # SC OPTIMISED TO O(1), altough not much readable
        row = len(matrix)
        col = len(matrix[0])

        col0 = 1

        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    if j == 0:
                        col0 = 0
                    else:
                        matrix[0][j] = 0
        
        for i in range(1,row):
            for j in range(1, col):
                if matrix[i][0] == 0 or matrix[0][j] ==0:
                    matrix[i][j] = 0

        if matrix[0][0] == 0:
            for j in range(col):
                matrix[0][j] = 0

        if col0 == 0:
            for i in range(row):
                matrix[i][0] = 0
        



        # O(N*M) TC AND O(M+N) SC
        # row = len(matrix)
        # col = len(matrix[0])

        # rowl = set()
        # coll = set()

        # for i in range(row):
        #     for j in range(col):
        #         if matrix[i][j] == 0:
        #             rowl.add(i)
        #             coll.add(j)
        
        # for i in range(row):
        #     for j in range(col):
        #         if i in rowl or j in coll:
        #             matrix[i][j] = 0

