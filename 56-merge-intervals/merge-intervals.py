class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        # TODO: later implement this wotout sort(), heap sort is an option
        intervals.sort(key = lambda i : i[0])
        output = [intervals[0]]

        for start, end in intervals[1:]:
            lastEnd = output[-1][1]

            if start <= lastEnd:
                # [1,5] , [2,4]
                output[-1][1] = max(lastEnd, end)
            else:
                # [1, 5], [7,8]
                output.append([start, end])
        return output
            