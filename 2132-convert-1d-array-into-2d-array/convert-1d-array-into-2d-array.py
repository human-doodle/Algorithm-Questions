class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        arr = [[0]*n for i in range(m)]
        print(len(original),n*m)
        if len(original)!=n*m :
            print('here')
            return []
        
        # one way
        # idx = 0
        # for row in range(m):
        #     for col in range(n):
        #         arr[row][col] = original[idx]
        #         idx+=1
        
        # second way
        for i, e in enumerate(original):
            arr[i // n][i % n] = e
        return arr