class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1
        while l<r:
            val = numbers[l] + numbers[r]
            if val == target:
                return [l+1, r+1]
            if val > target:
                r -= 1
            else:
                l += 1
        return []


'''   
Input: numbers = [2,7,11,15], target = 9
                  ^
Output: [1,2]
'''