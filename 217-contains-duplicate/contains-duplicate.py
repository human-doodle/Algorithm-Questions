class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Tried this way, but gives tle
        # d = []
        # for n in nums:
        #     if n in d:
        #         return True
        #     else:
        #         d.append(n)
        # return False
        d = dict()
        for n in nums:
            if n in d:
                return True
            else:
                d[n] = 1
        return False
