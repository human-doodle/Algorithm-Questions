class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n, m = len(matrix), len(matrix[0])
        zero_rows, zero_cols = set(), set()

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    zero_rows.add(i)
                    zero_cols.add(j)

        for i in range(n):
            for j in range(m):
                if i in zero_rows or j in zero_cols:
                    matrix[i][j] = 0
        