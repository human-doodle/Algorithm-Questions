class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        count = 0
        for ch in s:
            if ch == '1':
                count+=1
        return '1'*(count-1)+'0'*(len(s)-count)+'1'

        #O(n)