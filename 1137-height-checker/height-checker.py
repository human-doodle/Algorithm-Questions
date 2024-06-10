class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count = 0
        new = sorted(heights)
        for i in range(len(heights)):
            if heights[i]!=new[i]:
                count+=1
        return count

        