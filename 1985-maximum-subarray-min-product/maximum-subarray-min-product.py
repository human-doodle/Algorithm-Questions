class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        prefix = [0]
        res = 0
        stack = []
        N = len(nums)
        M = 10**9 + 7

        for n in nums:
            prefix.append(prefix[-1]+n)
        
        for i, num in enumerate(nums):
            newStart = i
            while stack and stack[-1][1]>num:
                start, val = stack.pop()
                total = prefix[i] - prefix[start]
                res = max(res, total*val)
                newStart = start
            stack.append((newStart, num))
        
        for start, val in stack:
            total = prefix[N] - prefix[start]
            res = max(res, total*val)
        
        return res % M
