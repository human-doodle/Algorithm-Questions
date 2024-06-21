# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def _flip_tree(root):
            if not root:
                return 
            root.right, root.left = root.left, root.right
            _flip_tree(root.left)
            _flip_tree(root.right)
        
        _flip_tree(root)
        return root
        
        # if not root:
        #     return 
        # q = collections.deque()
        # q.append(root)

        # while q:
        #     curr = q.popleft()

        #     if curr.left:
        #         q.append(curr.left) 

        #     if curr.right :
        #         q.append(curr.right) 

        #     curr.left, curr.right = curr.right, curr.left
            
        # return root

                
                


        
