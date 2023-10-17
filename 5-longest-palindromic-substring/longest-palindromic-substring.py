class Solution:
    def checkfromcenter(self, s, left, right):
        while left>=0 and right<len(s) and s[left] == s[right]:
            left-=1
            right+=1
        return s[left+1:right]
    def longestPalindrome(self, s: str) -> str:
        res = ''
        for i in range(len(s)):
            #for odd palindrom
            odd = self.checkfromcenter(s, i, i)
            if len(odd)>len(res):
                res = odd
            #even 
            even = self.checkfromcenter(s, i, i+1)
            if len(even)>len(res):
                res = even
        return res


        