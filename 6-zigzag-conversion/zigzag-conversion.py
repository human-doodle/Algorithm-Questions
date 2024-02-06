class Solution:
    def convert(self, s: str, numRows: int) -> str:
        k = 0
        row = ['' for _ in range(numRows)]
    
        while k < len(s):
            for i in range(numRows):
                if k >= len(s):
                    break
                row[i] += s[k]
                k += 1
            for i in range(numRows - 2, 0, -1):
                if k >= len(s):
                    break
                row[i] += s[k]
                k += 1
        return ''.join(row)
