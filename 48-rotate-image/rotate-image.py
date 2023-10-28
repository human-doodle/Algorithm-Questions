class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # transpose and reverse each row

        n = len(matrix)

        # transpose
        for i in range(0, n-1):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
       

        # reverse
        for i in range(0, n):
            matrix[i].reverse()
        
        