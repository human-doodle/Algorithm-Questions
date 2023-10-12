# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        stack = []
        curr = root
        prev, first, middle, last = TreeNode(-float('inf')), None, None, None
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            
            if prev and curr.val < prev.val:
                    if not first:
                        first = prev
                        middle = curr
                    else:
                        last = curr

            prev = curr
            curr = curr.right

        if last and first:
            last.val, first.val = first.val, last.val
        elif middle and first:
            middle.val, first.val = first.val, middle.val
         

        