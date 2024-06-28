class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefix = set()
        for x in arr1:
            c = str(x)
            for j in range(1, len(c)+1):
                prefix.add(c[:j])
        
        best = 0
        for x in arr2:
            c = str(x)
            for j in range(1, len(c)+1):
                if c[:j] in prefix:
                    best  = max(best, j)
        return best

        