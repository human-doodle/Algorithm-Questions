class Solution:
    def scoreOfString(self, s: str) -> int:
        l, r = 0,1
        score = 0
        while r<len(s):
            score += abs(ord(s[r])-ord(s[l]))
            r+=1
            l+=1
        return score

        