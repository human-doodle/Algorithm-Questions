class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s)-1
        while i<=j:
            while i<len(s) and not s[i].isalnum() :
                i+=1
            while j>=0  and not s[j].isalnum()  :
                j-=1
            if i<len(s) and j>=0 and s[i].lower() != s[j].lower():
                return False
            i+=1
            j-=1
        return True
        

'''
i+=1
while i.isAlphanum():
    i+=1
j+=1
while j.isAlphanum():
    j-=1   
Input: s = "A man, a plan, a canal: Panama"
              i                         j 
            no alphanumeric, upper->lowercase 
O(n) O(1)
Output: true

'''