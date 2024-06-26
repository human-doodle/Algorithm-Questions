class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        result = []
        h = []
        for point in points:
            x, y = point
            distance  = sqrt(x**2 + y**2)
            heapq.heappush(h, (distance, point))
        for i in range(k):
            distance, point = heapq.heappop(h)
            result.append(point)
        return result
            

        