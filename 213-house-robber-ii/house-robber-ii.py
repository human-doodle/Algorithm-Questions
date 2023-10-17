class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        def f(arr):
            if len(arr) == 0:
                return 0
            prev1 = 0
            prev2 = 0
            for i in range(len(arr)):
                temp = prev1
                prev1 = max(prev2+arr[i], prev1)
                prev2 = temp
            return prev1
        return max(f(nums[1:]), f(nums[:-1]))
        
        
        