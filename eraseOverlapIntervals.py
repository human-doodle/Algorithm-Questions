'''

leetcode link: https://leetcode.com/problems/non-overlapping-intervals/description/

435. Non-overlapping Intervals
Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

 

Example 1:

Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.
Example 2:

Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.
Example 3:

Input: intervals = [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
 

Constraints:

1 <= intervals.length <= 105
intervals[i].length == 2
-5 * 104 <= starti < endi <= 5 * 104

reference: https://www.youtube.com/watch?v=zPtI8q9gvX8

'''

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        # sort the intervals based on the ending time
        intervals.sort(key = lambda interval: interval[1])
        
        # interval with the largest end time seen so far
        largest_end_seen_so_far = intervals[0][1]
        
        # number of longest subset that don't overlap
        count = 1
        
        # loop over intervals
        for i in range(len(intervals)):

            # check if start time starts after largest_end_seen_so_far
            if intervals[i][0] >= largest_end_seen_so_far:
                # increment count
                count+=1
                # update the largest_end_seen_so_far
                largest_end_seen_so_far =  intervals[i][1]

        # return minimum number of intervals you need to remove to make the rest of the intervals non-overlapping
        return len(intervals) - count
