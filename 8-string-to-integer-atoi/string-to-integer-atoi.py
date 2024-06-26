class Solution:
    def myAtoi(self, s: str) -> int:
        '''
        1. whitw spaced
        2. +/- symbol
        3. e=between max_INT and min_INT CONSTRAINTS
        4. random characters

        '''
        res = 0
        i = 0
        negative = 1

        MAX_INT = 2**31 -1
        MIN_INT = - 2**31

        # remove whitw spaces
        while i < len(s) and s[i] == ' ':
            i+=1

        #sign
        if i<len(s) and s[i] == '-':
            i+=1
            negative = -1
        elif i<len(s) and s[i] == '+':
            i+= 1

        # number
        checker = set('0123456789')
        while i<len(s) and s[i] in checker:
            res = res*10 + int(s[i])
            i+=1
        
        res = res*negative
        if res<0:
            return max(res, MIN_INT)

        return min(res, MAX_INT)



        