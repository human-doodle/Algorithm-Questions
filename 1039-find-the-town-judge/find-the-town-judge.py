class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1 and trust == []:
            return 1
        d_trust = dict()
        d_inv_trust = dict()
        for [i, j] in trust:
            d_trust[i] = d_trust.get(i, 0) + 1
            d_trust[j] = d_trust.get(j, 0)

            d_inv_trust[i] = d_inv_trust.get(i, 0)
            d_inv_trust[j] = d_inv_trust.get(j, 0) + 1



        for key, value in d_trust.items():
            if value == 0 and d_inv_trust[key]==n-1:
                return key
        return -1

        # O(2N); O(N)
        