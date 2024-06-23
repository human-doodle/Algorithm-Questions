class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_d = deque()
        min_d = deque()
        
        left = 0
        result = 0
        
        for right in range(len(nums)):
            # Maintain the max deque
            while max_d and nums[right] > max_d[-1]:
                max_d.pop()
            max_d.append(nums[right])
            
            # Maintain the min deque
            while min_d and nums[right] < min_d[-1]:
                min_d.pop()
            min_d.append(nums[right])
            
            # Check the condition and adjust the left pointer
            while max_d[0] - min_d[0] > limit:
                if max_d[0] == nums[left]:
                    max_d.popleft()
                if min_d[0] == nums[left]:
                    min_d.popleft()
                left += 1
            
            result = max(result, right - left + 1)
        
        return result
