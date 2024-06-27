class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        g = {}
        for edge in edges:
            a, b = edge
            g[a] = g.get(a, [])
            g[a].append(b)
            g[b] = g.get(b, [])
            g[b].append(a)
        for node in g:
            if len(g[node])>1:
                return node
        