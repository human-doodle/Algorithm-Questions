class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:

        # iterative
        
        stack = [(root, 0)]
        postorder = []
        
        while stack:
            curr, visited = stack.pop()
            if curr:
                if visited:
                    if curr.val == 0 or curr.val == 1:
                        postorder.append(curr.val == 1)
                    else:
                        if curr.val == 2:
                            left = postorder.pop()
                            right = postorder.pop()
                            value = left or right
                            postorder.append(value)
                        elif curr.val == 3:
                            left = postorder.pop()
                            right = postorder.pop()
                            value = left and right
                            postorder.append(value)
                else:
                    stack.append((curr, 1))
                    stack.append((curr.right, 0))
                    stack.append((curr.left, 0))
            
        
        return postorder[0]