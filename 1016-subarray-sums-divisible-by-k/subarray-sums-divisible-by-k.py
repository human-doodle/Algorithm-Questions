class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # prefix
        prefix = {0:1}
        prev = 0
        count = 0
        for i in range(len(nums)):
            prev = prev+nums[i]
            mod = prev % k
            if mod < 0:  
                mod += k
            if mod in prefix:
                count += prefix[mod]
                prefix[mod] += 1
            else:
                prefix[mod] = 1
        return count
        