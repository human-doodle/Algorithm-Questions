class Solution:
    
    def subsets(self, nums: List[int]) -> List[List[int]]:

        if len(nums) == 0:
            return [[]]

        first = nums[0]
        exclude = self.subsets(nums[1:])

        include = []
        for sub in exclude:
            include.append([first,*sub])
        
        return include+exclude
