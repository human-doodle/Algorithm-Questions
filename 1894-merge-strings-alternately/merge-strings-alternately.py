class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j = 0, 0
        res = []
        count = 0

        while i<len(word1) and j<len(word2):
            if count % 2 == 0:
                res.append(word1[i])
                i+=1
                count+=1
            else:
                res.append(word2[j])
                j+=1
                count+=1

        if i<len(word1):
            res.append(word1[i:])
        if j<len(word2):
            res.append(word2[j:])
            
        return ''.join(res)
            