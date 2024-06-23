# nahi aaata

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0

        min_value, max_value = min(nums), max(nums)
        if min_value == max_value:
            return 0

        n = len(nums)
        bucket_size = max(1, (max_value - min_value) // (n - 1))
        bucket_count = (max_value - min_value) // bucket_size + 1

        buckets = [[None, None] for _ in range(bucket_count)]

        for num in nums:
            bucket_index = (num - min_value) // bucket_size
            if buckets[bucket_index][0] is None:
                buckets[bucket_index][0] = buckets[bucket_index][1] = num
            else:
                buckets[bucket_index][0] = min(buckets[bucket_index][0], num)
                buckets[bucket_index][1] = max(buckets[bucket_index][1], num)

        max_gap = 0
        previous_max = min_value
        for i in range(bucket_count):
            if buckets[i][0] is not None:
                max_gap = max(max_gap, buckets[i][0] - previous_max)
                previous_max = buckets[i][1]

        return max_gap
