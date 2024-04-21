class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        g = [[] for _ in range(n)]
        for u,v in edges:
            g[u].append(v)
            g[v].append(u)
        
        visited = set()
        def dfs(node):
            if node == destination:
                return True
            if node in visited:
                return False
            visited.add(node)
            for neighbor in g[node]:
                if dfs(neighbor):
                    return True
            
        return dfs(source)
