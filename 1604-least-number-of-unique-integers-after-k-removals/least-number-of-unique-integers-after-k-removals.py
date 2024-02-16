class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freq = dict()

        for num in arr:
            freq[num] = freq.get(num, 0) + 1
        
        sorted_freq = sorted(freq.values())
        
        idx = 0
        while k > 0 and idx < len(sorted_freq):

            if sorted_freq[idx]>=k:

                sorted_freq[idx] = sorted_freq[idx]-k
                k = 0

            else:
                balance = k - sorted_freq[idx]
                sorted_freq[idx] = 0
                k = balance
                
            idx+=1
        
        res = 0
        
        for element in sorted_freq:
            if element!=0:
                res+=1

        return res

# O(nlogn); O(n)

            