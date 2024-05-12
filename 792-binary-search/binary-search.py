class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # O(logn); O(1)
        def bs(arr, low, high, taget):
            
            while low<=high:
                mid = low+(high-low)//2
                if arr[mid] == target:
                    return mid
                elif arr[mid]>taget:
                    high = mid-1
                else:
                    low = mid+1
            return -1
        
        return bs(nums, 0, len(nums)-1, target)
        

'''
idx = -1
 [-1,0,3,5,9,12], 
         l.    h
 target = 9
Output: 4
'''