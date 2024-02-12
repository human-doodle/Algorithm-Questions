class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        
        # Brute force O(n) O(n)
        n = len(nums)
        d = dict()
        res = []
        for num in nums:
            d[num] = d.get(num, 0)+1
        
        for key in d.keys():
            if d[key]>n/3:
                res.append(key)
        
        return res
