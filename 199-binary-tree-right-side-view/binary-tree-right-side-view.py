# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def rightPath(node, path, level):
            if not node:
                return
            if level>= len(path):
                path.append(node.val)
            rightPath(node.right, path, level+1)
            rightPath(node.left, path, level+1)
            
        path = []
        rightPath(root, path, 0 )
        return path

