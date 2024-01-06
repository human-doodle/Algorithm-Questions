class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # brute force using dictioanry
        d = dict()
        for num in nums:
            if num in d:
                return num
            d[num] = 1
        

        