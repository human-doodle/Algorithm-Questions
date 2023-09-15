class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ind = {}
        for i, num in enumerate(nums):
            
            diff = target - num 
            if diff in ind:
                return [i, ind[diff]]
            ind[num] = i
        