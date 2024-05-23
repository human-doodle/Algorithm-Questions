class Solution:
    
    def trailingZeroes(self, n: int) -> int:
        # count number of 5s
        res = 0
        i = 5
        while n/i:
            fives = n // i
            i*=5
            res+=fives

        return res


            
        