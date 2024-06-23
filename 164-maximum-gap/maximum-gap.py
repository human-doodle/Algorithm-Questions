class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums)<2:
            return 0

        nums = sorted(set(nums))
        max_sum = 0
        for i in range(1, len(nums)):
            max_sum = max(max_sum, nums[i]-nums[i-1])
        return max_sum
        