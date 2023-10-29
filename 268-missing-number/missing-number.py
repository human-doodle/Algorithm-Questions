class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # O(3n) -> O(n) SC: O(n)
        d = {}
        for i in range(len(nums)+1):
            d[i] = 0
        for n in nums:
            d[n] = 1
        for k in d:
            if d[k] == 0:
                return k

        # TC O(n) SC(1) : problem can overflow since we are adding
        n = len(nums)
        # sum = n * (n+1)/2
        # sum_nums = sum(nums)
        # return sum - sum_nums

        # O(n) O(1) : XOR bit manipulation
        res = 0
        for i in nums:
            res^=i
        return res



        