class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # using not in or in results in tle
        # res = []
        # for n in range(1,len(nums)+1):
        #     if n in nums:
        #         continue

        #     res.append(n)
        # return res

        # using hash set
        res = []
        d = {i:0 for i in range(1, len(nums)+1)}
        for n in nums:
            d[n]+=1
        for k,v in d.items():
            if v==0:
                res.append(k)
        
        return res
        