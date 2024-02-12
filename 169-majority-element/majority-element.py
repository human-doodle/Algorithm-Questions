class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        d = dict()
        for num in nums:
            d[num] = d.get(num, 0) + 1
            if d[num] > n/2:
                return num
                    