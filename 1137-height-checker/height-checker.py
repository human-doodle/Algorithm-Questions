class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count = 0
        # new = sorted(heights)
        # count - sort
        new = []
        freq = {}
        for i in range(len(heights)):
            freq[heights[i]] = freq.get(heights[i], 0) + 1
        for i in range(1, 101):
            if i in freq:
                for j in range(freq[i]):
                    new.append(i)
        for i in range(len(heights)):
            if heights[i]!=new[i]:
                count+=1
        return count

        