class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        if n == 1:
            return [0]
        
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        leaves = [i for i in range(n) if len(graph[i]) == 1]
        
        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                parent = graph[leaf].pop()
                graph[parent].remove(leaf)
                if len(graph[parent]) == 1:
                    new_leaves.append(parent)
            leaves = new_leaves
        
        return leaves