class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        p = 0
        total_sum = nums[0] + nums[1]
        
        for x in nums[2:]:
            if total_sum > x:
                p = total_sum + x
            total_sum += x
        
        return p if p > 0 else -1