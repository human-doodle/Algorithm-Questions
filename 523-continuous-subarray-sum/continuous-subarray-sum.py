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
            
            
        # subarray startign at index i+1 and ending at j : prefix[j] - prefix[i]
        '''
        1, 2, 3
        ^.    ^
        1, 3, 6
        0, 1, 3
         prefix[j] - prefix[i] % k == 0
        prefix[j]%k == prefix[i] % k

        '''
        # # O(n^3) brute force TLE
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         _sum = sum(nums[i:j+1])
        #         if _sum%k == 0:
        #             return True
        # return False
        