class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
    
        def backtrack(index, freq_map):
            nonlocal count
            
            if index == len(nums):
                if len(freq_map) > 0:  # Ensure it's a non-empty subset
                    count += 1
                return
            
            # Option 1: Do not include nums[index] in the subset
            backtrack(index + 1, freq_map)
            
            # Option 2: Include nums[index] in the subset
            valid_to_add = True
            current_num = nums[index]
            
            if current_num - k in freq_map or current_num + k in freq_map:
                valid_to_add = False
            
            if valid_to_add:
                freq_map[current_num] += 1
                backtrack(index + 1, freq_map)
                freq_map[current_num] -= 1
                if freq_map[current_num] == 0:
                    del freq_map[current_num]
        
        count = 0
        freq_map = defaultdict(int)
        backtrack(0, freq_map)
        return count

