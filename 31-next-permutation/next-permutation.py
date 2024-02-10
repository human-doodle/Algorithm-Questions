class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        # Step 1
        k = n-2
        while k >= 0 and nums[k] >= nums[k+1]:
            k -= 1
        
        if k < 0:
            # Array is in descending order, reverse it
            nums.reverse() 
            return

        # Step 2
        l = n-1
        while l > k and nums[l] <= nums[k]:
            l -= 1
        
        # Step 3
        nums[k], nums[l] = nums[l], nums[k]
        
        # Step 4
        left = k+1
        right = n-1
        
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        