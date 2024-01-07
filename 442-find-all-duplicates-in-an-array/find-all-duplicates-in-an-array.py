class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # similar to dupkicate eklemnentz, challeniging to do in O(1) space
        # when you subtract one from nums elements, they are valid indexes due to the explicitely mentioned rsnge asnd constrains in the question
        # pigeon hole
        res = []
        for i in range(len(nums)):
            idx = abs(nums[i]) - 1
            if nums[idx] < 0:
                res.append(idx+1)
            nums[idx] = - nums[idx]
        
        return res


        