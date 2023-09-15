# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # bfs iterarive
        res = []
        q = collections.deque()
        q.append(root)
        while q:
            node = q.popleft()
            if not node:
                res.append('null')
                continue
            res.append(str(node.val))
            q.append(node.left)
            q.append(node.right)
        return ','.join(res) 
        # # preorder traversal - dfs
        # res = []
        # def dfs(node):
        #     if not node:
        #         res.append("null")
        #         return
        #     res.append(str(node.val))
        #     dfs(node.left)
        #     dfs(node.right)
        # dfs(root)
        # return ','.join(res)

        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # bfs iterative
        vals = data.split(',')
        if vals[0] == 'null':
            return None
        root = TreeNode(int(vals[0]))
        i = 1
        q = collections.deque()
        q.append(root)
        while q:
            node = q.popleft()

            # process left
            if vals[i]=="null":
                i+=1
                node.left = None
            else:
                leftnode = TreeNode(int(vals[i]))
                node.left = leftnode
                q.append(leftnode)
                i+=1

            # process right
            if vals[i]=="null":
                i+=1
                node.right = None
            else:
                rightnode = TreeNode(int(vals[i]))
                node.right = rightnode
                q.append(rightnode)
                i+=1
        return root
        # # preorder traversal - dfs
        # vals = data.split(',')
        # self.i = 0

        # def dfs():
        #     if vals[self.i]=='null':
        #         self.i+=1
        #         return None
        #     node = TreeNode(int(vals[self.i]))
        #     self.i+=1
        #     node.left = dfs()
        #     node.right = dfs()
        #     return node
        # return dfs()
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))