class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # prefix aray
        prefix_sum_mod_seen = {0 : -1}
        prev = 0

        for i in range(len(nums)):
            prev = (prev + nums[i]) % k
            
            if prev in prefix_sum_mod_seen:
                if i - prefix_sum_mod_seen[prev] > 1: # check if size of array >= 2
                    return True
            else:
                prefix_sum_mod_seen[prev] = i

        return False
            