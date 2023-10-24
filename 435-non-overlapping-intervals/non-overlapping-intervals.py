class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key= lambda i: i[1])
        print(intervals)
        last = intervals[0]
        res = 0
        for i in range(1, len(intervals)):
            if intervals[i][0]<last[1]:
                res+=1
            else:
                last = intervals[i]

        return res



        