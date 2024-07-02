class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d1 = {}
        d2 = {}

        res = []

        for i in nums1:
            d1[i] = d1.get(i, 0) + 1

        for i in nums2:
            d2[i] = d2.get(i, 0) + 1

        for k, v in d2.items():
            if k in d1:
                arr = [k]*min(v, d1[k])
                res = res + arr
                
        return res


