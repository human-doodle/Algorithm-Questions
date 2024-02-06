class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = {}
        for s in strs:
            sorted_s = "".join(sorted(s))
            if sorted_s not in d:
                d[sorted_s] = []
            d[sorted_s].append(s)
        return d.values()
