class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = dict()
        for i,ch in enumerate(s):
            if ch not in d:
                d[ch] = [i, 1]
                continue
            d[ch][1] = d[ch][1]+1
        
        for ch, [idx,freq] in d.items():
            if freq == 1:
                return idx
        
        return -1
        