class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = max(nums)
        currsum = 0
        for i in range(len(nums)-1, -1, -1):
            if currsum<0:
                currsum = 0
            currsum+=nums[i]
            res = max(currsum, res)
        return res