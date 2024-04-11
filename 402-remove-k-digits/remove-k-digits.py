class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        # Iterate through each digit in the number
        for digit in num:
            # While the stack is not empty, the current digit is less than the top digit of the stack,
            # and we still have remaining digits to remove
            while stack and k > 0 and digit < stack[-1]:
                stack.pop()  # Pop digits from the stack
                k -= 1       # Decrement k
                
            stack.append(digit)  # Add the current digit to the stack
        
        # After iterating through all the digits, if there are still remaining digits to remove
        # (k > 0), remove the last k digits from the stack
        while k > 0:
            stack.pop()
            k -= 1
        
        # Construct the resulting string by concatenating the digits in the stack
        result = ''.join(stack).lstrip('0') or '0'
        
        return result
                