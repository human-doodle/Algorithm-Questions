class Solution:
    def checkfromcenter(self, s, left, right):
        num= 0 
        while left>=0 and right<len(s) and s[right] == s[left]:
            right+=1
            left-=1
            num+=1
        return num
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            # odd
            odd = self.checkfromcenter(s, i, i)
            # even
            even = self.checkfromcenter(s, i, i+1)
            res = res+odd+even
        return res