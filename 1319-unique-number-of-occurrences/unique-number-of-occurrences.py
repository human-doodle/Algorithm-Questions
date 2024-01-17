class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = dict()
        s = set()
        for num in arr:
            if num not in d:
                d[num] = 1
            d[num] += 1
        for key, value in d.items():
            if value in s:
                return False
            s.add(value)
        return True
            
        