class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        N = len(heights)
        res = 0
        stack = []
        # prefix = [0]

        for i, height in enumerate(heights):
            newStart = i
            while stack and stack[-1][1]>height:
                start, val = stack.pop()
                area = val * (i-start)
                res = max(area, res)
                newStart = start
            stack.append((newStart, height))
        
        for start, val in stack:
            area = val * (N-start)
            res = max(area, res)
        
        return res
