class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        # Calculate the initial sum of all node values
        initial_sum = sum(nums)
        
        # Initialize variables to track total gain, count of positive gains, and the minimum absolute gain
        total_gain = 0
        positive_gain_count = 0
        min_abs_gain = float('inf')
        
        for num in nums:
            gain = (num ^ k) - num
            
            if gain > 0:
                total_gain += gain
                positive_gain_count += 1
            min_abs_gain = min(min_abs_gain, abs(gain))
        
        # Adjust total_gain if positive_gain_count is odd
        if positive_gain_count % 2 == 1:
            total_gain -= min_abs_gain
        
        # Return the final maximum sum
        return initial_sum + total_gain
