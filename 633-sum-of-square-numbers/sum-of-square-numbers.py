class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i, j = 0, floor(sqrt(c))
        while i<=j:
            sum_of_square = i*i + j*j
            if sum_of_square == c:
                return True
            if sum_of_square<c:
                i+=1
            else:
                j-=1
        return False
    