# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node, path, res):
        if not node:
            return

        if not node.right and not node.left:
            path += str(node.val)
            res.append(path)
           
        path += str(node.val)+'->'
        self.dfs(node.right, path, res)
        self.dfs(node.left, path, res)


    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        self.dfs(root, "", res)
        return res

        