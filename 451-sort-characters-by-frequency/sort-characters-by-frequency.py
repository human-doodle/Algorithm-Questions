class Solution:
    def frequencySort(self, s: str) -> str:
        res= ""
        freq = dict()
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1
        
        h = []
        for key, value in freq.items():
            heapq.heappush(h, (-value, key))
        
        for i in range(len(freq.keys())):
            value, ch = heapq.heappop(h)
            res += ch*(-value)
        
        return res
        