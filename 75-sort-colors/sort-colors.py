class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # only 3 colors
        count = {0:0, 1:0, 2:0}
        for num in nums:
            count[num]+=1
        for i in range(0 , count[0]):
            nums[i] = 0  
        for i in range(count[0], count[0]+ count[1]):
            nums[i] = 1
        for i in range(count[0]+count[1], count[0]+count[1]+count[2]):
            nums[i] = 2    