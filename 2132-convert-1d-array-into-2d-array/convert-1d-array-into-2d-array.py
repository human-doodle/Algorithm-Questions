class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        arr = [[0]*n for i in range(m)]
        if len(original)>n*m or len(original)<n*m:
            return []
        idx = 0
        for row in range(m):
            for col in range(n):
                arr[row][col] = original[idx]
                idx+=1
        
        return arr
        