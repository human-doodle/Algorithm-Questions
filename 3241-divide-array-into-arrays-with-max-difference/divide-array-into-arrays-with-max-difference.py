class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        array_size = len(nums)
        nums.sort()

        result = []
        # greedy
        for i in range(0, array_size, 3):
            # Check if there are at least three elements in the current group
            if not (i + 2 < array_size and nums[i + 2] - nums[i] <= k):
                return []
            result.append([nums[i], nums[i + 1], nums[i + 2]])
        return result