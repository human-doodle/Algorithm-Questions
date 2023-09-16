class MedianFinder:

    def __init__(self):
        # large elements
        self.minheap = []
        # small elements
        self.maxheap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxheap, -num)

        # make sure every elemnt is small is less tahn large heap
        if self.minheap and self.maxheap and (self.minheap[0]<-self.maxheap[0]):
            val = heapq.heappop(self.maxheap)
            heapq.heappush(self.minheap, -val)
        # uneven size
        if len(self.maxheap)>len(self.minheap):
            val = heapq.heappop(self.maxheap)
            heapq.heappush(self.minheap, -val)
        if len(self.minheap)>len(self.maxheap):
            val = heapq.heappop(self.minheap)
            heapq.heappush(self.maxheap, -val)
        

    def findMedian(self) -> float:
        if len(self.minheap)>len(self.maxheap):
            return self.minheap[0]
        if len(self.maxheap)>len(self.minheap):
            return -self.maxheap[0]
        return (self.minheap[0]-self.maxheap[0])/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()