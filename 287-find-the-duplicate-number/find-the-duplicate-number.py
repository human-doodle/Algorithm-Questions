class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # brute force using dictioanry using non constant space
        # d = dict()
        # for num in nums:
        #     if num in d:
        #         return num
        #     d[num] = 1
        
        # constant space...
        # must knwo: Floyd's circle detection algorithm and imagine list as linked list if unique numbers

        slow, fast = 0,0
        while True:
            slow = nums[slow]
            fast  = nums[nums[fast]]
            if slow == fast:
                break
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow        




        