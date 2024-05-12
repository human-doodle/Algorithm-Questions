class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # O(n); O(2n)
        if len(s)!=len(t):
            return False

        counterS = dict()
        counterT = dict()
        for i in range(len(s)):
            counterS[s[i]] = counterS.get(s[i], 0)+1
            counterT[t[i]] = counterT.get(t[i], 0)+1
        
        return counterS == counterT

        # # o(nlogn) #O(1)
        # return sorted(s) == sorted(t)