"""

Leetcode Link: https://leetcode.com/problems/single-number/description/

136. Single Number

#bit_manipulation

"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # XOR of same numbers give 0, ie, 1 XOR 1 = 0 and 0 XOR 0 = 0
        # thus the reamaining number of XOR operation is the number with only 1 occurance 
        
        # Time: O(n)
        # Space: O(1)

        xor = 0
        for num in nums:
            xor = num ^ xor
        return xor
            
