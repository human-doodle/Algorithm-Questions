class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        prev2 = 0
        prev1 = 0
        for i in range(len(nums)):
            tmp = prev1
            prev1 = max(prev2 + nums[i], prev1)
            prev2 = tmp
        return prev1