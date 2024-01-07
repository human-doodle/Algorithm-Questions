class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # can use set, but will take extra space, but can use pegeoin hole, ignore negaticve values sincethey are anyways not positiv, so will change it to 0
        for i  in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0

        for i in range(len(nums)):
            val = abs(nums[i])
            if 1<=val<=len(nums):
                if nums[val - 1] > 0:
                    nums[val-1] *= -1
                elif nums[val - 1] == 0:
                    # because this is anyways the possible answer in worst case
                    nums[val - 1] = -1 * (len(nums) + 1)

        for i in range(1, len(nums)+1):
            if nums[i-1] >= 0:
                return i
        
        return len(nums)+1

# SC: O(1)
# TC: O(n)



                
        