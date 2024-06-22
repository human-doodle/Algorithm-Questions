class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        for i, num in enumerate(nums):
            if num%2 == 0:
                nums[i] = 0
            else:
                nums[i]= 1

        prefix_sum = 0
        count = 0
        prefix_counts = {0: 1}  # To handle the case where prefix_sum - goal == 0

        for num in nums:
            prefix_sum += num
            if prefix_sum - k in prefix_counts:
                count += prefix_counts[prefix_sum - k]
            if prefix_sum in prefix_counts:
                prefix_counts[prefix_sum] += 1
            else:
                prefix_counts[prefix_sum] = 1

        return count

        # tcn^3
        # count = 0
        # for i, num in enumerate(nums):
        #     if num%2 == 0:
        #         nums[i] = 0
        #     else:
        #         nums[i]= 1
        # for i in range(len(nums)):
        #     for j in range(i, len(nums)):
        #         if sum(nums[i:j+1]) == k:
        #             count+=1

        # return count