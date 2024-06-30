class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n
        self.count = n  # Count of connected components
    
    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]
    
    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        
        if root_u == root_v:
            return False
        
        if self.rank[root_u] > self.rank[root_v]:
            self.parent[root_v] = root_u
        elif self.rank[root_u] < self.rank[root_v]:
            self.parent[root_u] = root_v
        else:
            self.parent[root_v] = root_u
            self.rank[root_u] += 1
        
        self.count -= 1
        return True
    
    def connected_components(self):
        return self.count

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        # Initialize UnionFind structures for Alice and Bob
        alice_uf = UnionFind(n)
        bob_uf = UnionFind(n)
        
        remove_count = 0
        # Step 1: Process type 3 edges first
        for edge_type, u, v in edges:
            if edge_type == 3:
                if not (alice_uf.union(u - 1, v - 1) and bob_uf.union(u - 1, v - 1)):
                    remove_count += 1
        
        # Step 2: Process type 1 and type 2 edges
        for edge_type, u, v in edges:
            if edge_type == 1:
                if not alice_uf.union(u - 1, v - 1):
                    remove_count += 1
            elif edge_type == 2:
                if not bob_uf.union(u - 1, v - 1):
                    remove_count += 1
        
        # Step 3: Check if both Alice and Bob can traverse the entire graph
        if alice_uf.connected_components() > 1 or bob_uf.connected_components() > 1:
            return -1
        
        return remove_count

