class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # O(3n) -> O(n)
        d = {}
        for i in range(len(nums)+1):
            d[i] = 0
        for n in nums:
            d[n] = 1
        for k in d:
            if d[k] == 0:
                return k


        