class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        depth = 0
        d=0
        for i in s:
            if i=='(':
                d+=1
            elif i==')':
                d-=1
            else:
                pass
            depth = max(depth, d)
        return depth