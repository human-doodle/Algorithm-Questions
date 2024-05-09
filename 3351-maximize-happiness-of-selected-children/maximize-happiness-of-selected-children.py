class Solution(object):
    def maximumHappinessSum(self, happiness, k):
        """
        :type happiness: List[int]
        :type k: int
        :rtype: int
        """
        res = 0
        happiness.sort(reverse = True)
        for i in range(k):
            if happiness[i]-i>0:
                res+=(happiness[i]-i)
                
        return res
        # brute force
        # res = 0
        # happiness.sort(reverse = True)
        # for i in range(k):
        #     for j in range(i, len(happiness)):
        #         if j==i and happiness[j]>0:
        #             res+= happiness[j]
        #             continue
        #         happiness[j]-=1
        # return res
                


        