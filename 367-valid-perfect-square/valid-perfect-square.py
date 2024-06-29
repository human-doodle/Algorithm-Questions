class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left, right = 0, num
        while left<=right:
            mid = left + (right-left)//2
            if mid**2 > num:
                right = mid - 1
                
            elif mid **2 < num:
                left = mid + 1
                
            else:
                return True
        return False