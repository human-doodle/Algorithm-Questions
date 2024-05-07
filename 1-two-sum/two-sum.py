class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, num in enumerate(nums):
            n = target - num
            for j, num2 in enumerate(nums):
                if n == num2 and i!=j:
                    return [i,j]
        
        