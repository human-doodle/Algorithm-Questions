    """
Implement a Graph class that has a method route which finds a route between any two
given nodes. A Graph object is initialized by passing it two arguments n and edges, where n is the number
of nodes in the graph (you may assume all the nodes will be identified with numbers between 0 and n-1),
and edges is a list of tuples. Each tuple (src, dst) represents a directed edge between src and dst. The
route method takes two nodes src and dst as arguments and returns a path between them if one exists.
A path is just a list of edges (n0, n1), (n1, n2), (n2, n3)...(nk−1, nk), such that n0 is the source and nk is the
destination.
If such a path doesn’t exist, you just return an empty list.
Examples
>>> g1 = Graph(4, [(0, 1), (1, 2), (0, 2), (2, 3)])
>>> g1.route(1, 0)
[]
There is no route between 1 and 0.
>>> g1.route(0, 3)
[(0, 1), (1, 2), (2, 3)]
Another possible answer is [(0, 2), (2, 3)]
    """


class Graph:
    def __init__(self, n, edges):
        # consruct an adjacency list
        self.adj_list = [[] for _ in range(n)]

        # populate the adjacency list sunc that the array at index i
        #  contains the nodes which are the destination to i
        for src, dst in edges:
            self.adj_list[src].append(dst)
            print(src, dst)
        
        print(self.adj_list)
    

    
    def route(self, src, dst):

        # mark all nodes from the node at index i not visited
        visited = [False] * len(self.adj_list)
        
        path = []

        # call dfs
        if self._dfs(src, dst, visited, path):
            return path
        # did not find path, return empty array
        else:
            return []
    
    # dfs function to find path
    def _dfs(self, current, dst, visited, path):
        # once visited, mark true 
        visited[current] = True
        # if current node is the destination, return True
        if current == dst:
            return True
        # else for every neighbor of the ith node, if not vosited, add to the path (current and neighbor)
        print(current, self.adj_list[current])
        for neighbor in self.adj_list[current]:
            print(visited, neighbor)
            if not visited[neighbor]:
                
                path.append((current, neighbor))
                if self._dfs(neighbor, dst, visited, path):
                    return True
                # if the destination was't reachable 
                # from that path, pop the traversal to the last neighbor
                path.pop()
        return False
