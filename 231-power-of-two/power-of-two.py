class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <=0:
            return False
        while n >0:
            if n == 1:
                return True
            r = n%2
            if r!=0:
                print(n, r)
                return False
            n = n/2
        return True
        