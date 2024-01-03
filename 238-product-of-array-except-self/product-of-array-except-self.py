class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lm = []
        rm = []
        l, r = 1, 1

        for num in nums:
            lm.append(l)
            l*=num

        for num in nums[::-1]:
            rm.append(r)
            r*=num
        rm = rm[::-1]
        for i in range(len(nums)):
            nums[i] = lm[i]*rm[i]
        
        return nums

        