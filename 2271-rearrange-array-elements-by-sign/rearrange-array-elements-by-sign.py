class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # Separate positive and negative integers
        positive_nums = [num for num in nums if num > 0]
        negative_nums = [num for num in nums if num < 0]

        result = []

        # Alternate positive and negative integers in the result array
        for pos, neg in zip(positive_nums, negative_nums):
            result.extend([pos, neg])

        return result