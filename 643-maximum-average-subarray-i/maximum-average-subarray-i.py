class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # sliding window
        currentSum = maxSum = sum(nums[:k])
        for windowEnd in range(k, len(nums)):
            currentSum += nums[windowEnd] - nums[windowEnd-k]
            maxSum = max(currentSum, maxSum)
        return maxSum / k
        