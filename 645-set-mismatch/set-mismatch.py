class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        l = len(nums)
        s = set()
        res = []
        for n in nums:
            if n in s:
                res.append(n)
            s.add(n)
        
        for n in range(1, l+1):
            if n not in nums:
                res.append(n)
        return res     
        
    # 1,2,3,4
    # 1,2,2,4
    # 1, 2, 
        