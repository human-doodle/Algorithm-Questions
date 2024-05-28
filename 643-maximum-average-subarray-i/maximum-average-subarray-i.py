class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # sliding window
        i, j = 0, k
        maxavg = -float('inf')
        sum = 0
        for offset in range(k):
            sum+=nums[i+offset]
        maxavg = max(maxavg, sum/k)
        
        while j<len(nums):
            sum = sum-nums[i]+nums[j]
            maxavg = max(maxavg, sum/k)
            i+=1
            j+=1

        return maxavg
        
        