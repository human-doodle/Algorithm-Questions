class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        # KADANE'S ALGORITHM O(n) ; O(1)
        maxsum = -float('inf')
        curr_sum = 0

        for i in range(len(nums)):
            curr_sum += nums[i]
            maxsum = max(maxsum, curr_sum)

            # reinitializing to zero, because negative sum adds no value
            if curr_sum <= 0:
                curr_sum = 0
        
        return maxsum 
        