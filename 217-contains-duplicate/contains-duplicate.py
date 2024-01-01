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

        # this was successul - > hashset/dictionary is always better than array.
        # d = dict()
        # for n in nums:
        #     if n in d:
        #         return True
        #     else:
        #         d[n] = 1
        # return False

        # can also do using set
        d = set()
        for n in nums:
            if n in d:
                return True
            else:
                d.add(n)
        return False

