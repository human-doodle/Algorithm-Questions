'''


LEETCODE: 1614. Maximum Nesting Depth of the Parentheses

A string is a valid parentheses string (denoted VPS) if it meets one of the following:

It is an empty string "", or a single character not equal to "(" or ")",
It can be written as AB (A concatenated with B), where A and B are VPS's, or
It can be written as (A), where A is a VPS.
We can similarly define the nesting depth depth(S) of any VPS S as follows:

depth("") = 0
depth(C) = 0, where C is a string with a single character not equal to "(" or ")".
depth(A + B) = max(depth(A), depth(B)), where A and B are VPS's.
depth("(" + A + ")") = 1 + depth(A), where A is a VPS.
For example, "", "()()", and "()(()())" are VPS's (with nesting depths 0, 1, and 2), and ")(" and "(()" are not VPS's.

Given a VPS represented as string s, return the nesting depth of s.

link: https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/


'''

# using stack

class Solution:
    def maxDepth(self, s: str) -> int:
        depth = 0
        stack = []
        for i in s:
            if(i=='('):
                stack.append(i)
                depth = max(depth, len(stack))
            elif i==')':
                stack.pop()
            else:
                pass
        return depth
      
# better space complexity: O(1)

# class Solution:
#     def maxDepth(self, s: str) -> int:
#         depth = 0
#         d = 0
#         for i in s:
#             if(i=='('):
#                 d+=1
#                 depth = max(depth, d)
#             elif i==')':
#                 d-=1
#             else:
#                 pass
#         return depth
