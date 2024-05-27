class Solution:
    def specialArray(self, nums: List[int]) -> int:
        # sort and binary 
        nums.sort()
        left, right = 0, len(nums)
        while(left<=right):
            mid = left+(right-left)//2
            count = 0
            for num in nums:
                if num>=mid:
                    count+=1
            if mid == count:
                return mid
            elif mid>count:
                right = mid-1
            else:
                left = mid+1
        return -1

        # # O(n^2); O(1)
        # for i in range(len(nums)+1):
        #     count = 0
        #     for num in  nums:
        #         if num>=i:
        #             count+=1
        #     if count == i:
        #         return i
        # return -1

            
        