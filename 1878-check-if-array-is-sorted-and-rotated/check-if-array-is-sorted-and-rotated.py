class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)

        # Function to check if the array is sorted in non-decreasing order
        def isSorted(arr):
            return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))

        # Find the index where the rotation occurs
        rotation_index = 0
        for i in range(1, n):
            if nums[i] < nums[i - 1]:
                rotation_index = i
                break

        # Check if the array is sorted in non-decreasing order after rotation
        rotated_array = nums[rotation_index:] + nums[:rotation_index]
        return isSorted(rotated_array)