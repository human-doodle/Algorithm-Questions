class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for num in nums:
            d[num] = d.get(num, 0) + 1

        minHeap = []
        for num, v in d.items():
            heapq.heappush(minHeap, (-v, num))

        return [heapq.heappop(minHeap)[1] for _ in range(k)]
        