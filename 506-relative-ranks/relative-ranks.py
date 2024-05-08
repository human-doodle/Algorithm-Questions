class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        # brute force:
        res = []
        d = {}
        score_sorted = sorted(score)
        rank = 1
        for s in score_sorted[::-1]:
            d[s] = rank
            rank+=1
        for s in score:
            if d[s] == 1:
                res.append("Gold Medal")
            elif d[s] == 2:
                res.append("Silver Medal")
            elif d[s] == 3:
                res.append("Bronze Medal")
            else:
                res.append(str(d[s]))
        return res
