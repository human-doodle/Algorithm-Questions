'''
Leetcode: https://leetcode.com/problems/palindrome-number/description/
9. Palindrome Number

Given an integer x, return true if x is a palindrome, and false otherwise.

'''

class Solution:
    def isPalindrome(self, x: int) -> bool:

        # negative number will always be a non-palindrome
        if x < 0:
            return False
        
        # palindrome: reads same forwards and backwards
        x_reversed = 0
        temp = x

        # reverse the integer
        while temp != 0:
            x_reversed = x_reversed * 10 + temp % 10
            temp //= 10

        # check if equal and return
        return x_reversed == x
