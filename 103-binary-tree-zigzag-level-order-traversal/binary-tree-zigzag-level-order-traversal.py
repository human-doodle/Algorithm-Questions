# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # bfs itertative
        if not root:
            return

        q = collections.deque()
        q.append((root, 0))
        lastLevel = 0
        curr_level = []
        res = []

        while q:
            curr, level = q.popleft()
            # print(curr.val, level)
            if level!=lastLevel:
                if (lastLevel)%2 == 0:
                    res.append(curr_level)
                else:
                    res.append(curr_level[::-1])
                lastLevel += 1
                curr_level = [curr.val]
            else:
                curr_level.append(curr.val)

            if curr.left:
                    q.append((curr.left, level+1))
            if curr.right:
                    q.append((curr.right, level+1))
            
        if not q and curr_level:
            if (lastLevel)%2 == 0:
                    res.append(curr_level)
            else:
                    res.append(curr_level[::-1])

        print(curr_level)     
        return res

'''
bfs
lastLevel  = 0
if level!=lastLevel
    lastLevel+=1
    res.append([curr.val])
else:
    res[level].append(curr.val)
'''