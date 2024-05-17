# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if not root:
            return root
        # iterative
        
        stack = [(root, None, False)]


        while stack:
            curr, parent, visited = stack.pop()
            if curr:
                if visited:
                    if curr.val == target and not curr.right and not curr.left:
                        if root == curr:
                            del root
                            return 
                        if parent.right == curr:
                            parent.right = None
                        else:
                            parent.left = None
                        del curr
                else:
                    stack.append((curr, parent, True))
                    stack.append((curr.right, curr, False))
                    stack.append((curr.left, curr, False))
            
        return root

