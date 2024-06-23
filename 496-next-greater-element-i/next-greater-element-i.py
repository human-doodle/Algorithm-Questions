class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        d = {}
        res = [-1]*len(nums1)
        for i, num in enumerate(nums1):
            d[num] = i
        for num in nums2:
            while stack and stack[-1]<num:
                val = stack.pop()
                res[d[val]] = num
            if num in d:
                stack.append(num)
        return res