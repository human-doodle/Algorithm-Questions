# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def get_path(node, target):
            if not node:
                return None
            if node is target:
                return [node]
            left_path =  get_path(node.left, target)
            if left_path:
                left_path.append(node)
                return left_path
            right_path =  get_path(node.right, target)
            if right_path:
                right_path.append(node)
                return right_path

            return None

        path1 = get_path(root, p)
        path2 = get_path(root, q)
        s = set(path1)
        for val in path2:
            if val in s:
                return val
        return None

