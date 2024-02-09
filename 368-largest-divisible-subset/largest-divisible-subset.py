class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
            
        if not nums:
            return []

        nums.sort()
        n = len(nums)
        dp = [1] * n  # dp[i] represents the size of the largest subset ending at index i
        prev_index = [-1] * n  # to reconstruct the subset

        max_size, max_index = 1, 0

        for i in range(1, n):
            for j in range(i - 1, -1, -1):
                if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    prev_index[i] = j

            if dp[i] > max_size:
                max_size = dp[i]
                max_index = i

        # Reconstruct the subset
        result = []
        while max_index != -1:
            result.append(nums[max_index])
            max_index = prev_index[max_index]

        return result[::-1]
