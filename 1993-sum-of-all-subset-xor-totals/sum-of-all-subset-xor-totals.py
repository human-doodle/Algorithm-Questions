class Solution:
    def subsetXORSum(self, nums):
        n = len(nums)
        total = 0
        for i in range(1, 1 << n):
            curr_total = 0
            for j in range(n):
                if i & (1 << j):
                    curr_total ^= nums[j]
            total += curr_total
        return total