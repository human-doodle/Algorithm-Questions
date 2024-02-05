class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if start> destination:
            start, destination = destination, start #doesnt make a difference
        pathsum, totalsum = 0,0
        for i in range(len(distance)):
            if i>=start and i<destination:
                pathsum += distance[i]
            totalsum += distance[i]
        return min(pathsum, totalsum-pathsum) # totalsum-pathsum is the distance got the other way
        
        
        
        