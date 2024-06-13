class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # dutch flag algorithm
        low, mid, high = 0, 0, len(nums)-1

        while mid<=high:
            if nums[mid] == 0:
                nums[mid], nums[low] = nums[low], nums[mid]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1

        # # only 3 colors O(2n); O(1)
        # count = {0:0, 1:0, 2:0}
        # for num in nums:
        #     count[num]+=1
        # for i in range(0 , count[0]):
        #     nums[i] = 0  
        # for i in range(count[0], count[0]+ count[1]):
        #     nums[i] = 1
        # for i in range(count[0]+count[1], count[0]+count[1]+count[2]):
        #     nums[i] = 2    