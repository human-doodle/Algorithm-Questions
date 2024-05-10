class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # O(n*m) O(1)
        l = len(needle)
        for i,s1 in enumerate(haystack):
            # O(m) for string comparision
            if haystack[i:i+l] == needle:
                return i
            
        return -1



        