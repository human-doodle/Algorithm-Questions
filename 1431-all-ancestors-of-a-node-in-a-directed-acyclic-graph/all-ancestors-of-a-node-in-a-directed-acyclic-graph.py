class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        def create_inverted_graph(edges):
            graph = {}
            for a, b in edges:
                graph[b] = graph.get(b, [])
                graph[b].append(a)
            return graph

        def find_ancestors(node, inverted_graph, memo):
            if node in memo:
                return memo[node]
            ancestors = set()
            for parent in inverted_graph.get(node, []):
                ancestors.add(parent)
                ancestors.update(find_ancestors(parent, inverted_graph, memo))
                
            memo[node] = ancestors
            return ancestors

            
        inverted_graph = create_inverted_graph(edges)

        # list to store the ancestors
        res = []
        memo = {}
        
        for i in range(n):
            ancestors = find_ancestors(i, inverted_graph, memo)
            res.append(sorted(ancestors))
        return res
