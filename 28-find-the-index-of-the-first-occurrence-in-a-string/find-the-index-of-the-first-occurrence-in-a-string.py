class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        res = -1
        l = len(needle)
        for i,s1 in enumerate(haystack):
            if haystack[i:i+l] == needle:
                return i
            
        return res



        