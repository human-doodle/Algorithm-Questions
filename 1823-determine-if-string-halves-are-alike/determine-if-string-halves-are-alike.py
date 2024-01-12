class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        def checkVowel(c):
            if c.lower() in ['a', 'e', 'i', 'o', 'u']:
                return True
            return False
        l = len(s)//2 
        a = 0
        b = 0
        for c in s[:l]:
            if value:=checkVowel(c):
                a+=1
                print(a)
        for c in s[l:len(s)]:
            if value:=checkVowel(c):
                b+=1
                print(b)
        if a==b:
            return True
        return False
        