class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        def rev(n):
            return int(str(n)[::-1])
        nums = [n - rev(n) for n in nums]
        ans = 0
        for n in Counter(nums).values():
            ans += n*(n-1)//2 
        return ans % (10**9 + 7)

        