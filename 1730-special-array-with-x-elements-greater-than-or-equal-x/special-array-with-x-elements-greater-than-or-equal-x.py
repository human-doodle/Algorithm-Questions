class Solution:
    def specialArray(self, nums: List[int]) -> int:
        # O(n^2); O(1)
        for i in range(len(nums)+1):
            count = 0
            for num in  nums:
                if num>=i:
                    count+=1
            if count == i:
                return i
        return -1

            
        