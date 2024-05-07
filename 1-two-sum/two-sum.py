class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, num in enumerate(nums):
            n = target - num
            if n in nums:
                j = nums.index(n)
                if j!=i:
                    return [i,j]
        # for i, num in enumerate(nums):
        #     n = target - num
        #     for j, num2 in enumerate(nums):
        #         if n == num2 and i!=j:
        #             return [i,j]
        
        