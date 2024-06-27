class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        res = 0
        s.sort()
        g.sort()
        i, j = 0, 0
    
        for i in range(len(g)):
            for j in range(len(s)):
               if g[i]<=s[j]:
                   g[i], s[j] = -1, -1
                   res+=1
                   break
        return res
                
