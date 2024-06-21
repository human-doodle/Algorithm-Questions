class Solution:
    
    def subsets(self, nums: List[int]) -> List[List[int]]:

        # def backtrack(start, path):
        #     res.append(path)
        #     for i in range(start, len(nums)):
        #         backtrack(i + 1, path + [nums[i]])
    
        # res = []
        # backtrack(0, [])
        # return res
        if len(nums) == 0:
            return [[]]

        first = nums[0]
        exclude = self.subsets(nums[1:])

        include = []
        for sub in exclude:
            include.append([first,*sub])
        
        return include+exclude
