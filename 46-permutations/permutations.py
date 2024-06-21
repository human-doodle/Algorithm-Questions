class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        first = nums[0]
        perms = self.permute(nums[1:])
        result = []
        for perm in perms:
            for i in range(len(perm)+1):
                result.append([*perm[:i], first, *perm[i:]])
        return result
        