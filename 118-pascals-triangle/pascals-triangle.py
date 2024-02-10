class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        def gen_nth_row(n: int)->List[int]:
            '''
            Generates n'th row
            '''
            temp = 1
            res = [temp]
            for i in range(1, n):
                temp = temp * (n-i)
                temp = temp // i
                res.append(temp)
            return res
        
        answer = []
        for i in range(1, numRows+1):
            answer.append(gen_nth_row(i))
        
        return answer
        # TC: O(n^2) 

        