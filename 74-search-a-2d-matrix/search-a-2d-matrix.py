class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        M = len(matrix)
        N = len(matrix[0])

        # optimal solution O(log(N+M)); O(1)
        def bs(matrix, target, M, N):
            n = M*N
            low, high = 0, n-1
            while low <= high:
                mid = ( high + low )//2
                if matrix[mid//N][mid%N] == target:
                    return True
                elif target > matrix[mid//N][mid%N]:
                    low = mid + 1
                else:
                    high = mid - 1
            return False

        return bs(matrix, target, M, N)


        # better:  find row and then binary search O(M + logN); O(1)
        # def bs(arr, target):
        #     n = len(arr)
        #     low, high = 0, n-1
        #     while low <= high:
        #         mid = ( high + low )//2
        #         if arr[mid] == target:
        #             return True
        #         elif target > arr[mid]:
        #             low = mid + 1
        #         else:
        #             high = mid - 1
        #     return False
        
        # for i in range(M):
        #     if matrix[i][0]<=target and matrix[i][N-1]>=target:
        #         return bs(matrix[i], target)

        # return False

        # brute force : O(M*N); O(1)
        
        # for i in range(M):
        #     for j in range(N):
        #         if matrix[i][j] == target:
        #             return True
        # return False
        