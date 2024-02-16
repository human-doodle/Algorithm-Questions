class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        d = dict()
        for num in arr:
            d[num] = d.get(num, 0) + 1
        
        d = [v for k, v in sorted(d.items(), key=lambda item: item[1])]
        print(d)
        idx = 0
        while k>0 and idx<len(d):
            if d[idx]>=k:
                d[idx] = d[idx]-k
                k = 0
            else:
                balance = k-d[idx]
                d[idx] = 0
                k = balance
            idx+=1
        
        res= 0
        
        for i in d:
            if i !=0:
                res+=1

        return res

# O(nlogn); O(n)

            