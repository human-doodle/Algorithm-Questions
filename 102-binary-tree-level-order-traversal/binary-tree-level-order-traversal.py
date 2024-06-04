# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        stack = [(root, 0)]
        res = []
        while stack:
            curr, level = stack.pop()

            if level == len(res):
                res.append([curr.val])
            else:
                res[level].append(curr.val)

            if curr.right:
                stack.append((curr.right, level+ 1))
            if curr.left:
                stack.append((curr.left, level + 1))
            
        return res
            