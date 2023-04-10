"""

#graph #connected componenr #adjacency list

link : https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/description/

947. Most Stones Removed with Same Row or Column

On a 2D plane, we place n stones at some integer coordinate points. Each coordinate point may have at most one stone.

A stone can be removed if it shares either the same row or the same column as another stone that has not been removed.

Given an array stones of length n where stones[i] = [xi, yi] represents the location of the ith stone, return the largest possible number of stones that can be removed.

 

Example 1:

Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
Output: 5
Explanation: One way to remove 5 stones is as follows:
1. Remove stone [2,2] because it shares the same row as [2,1].
2. Remove stone [2,1] because it shares the same column as [0,1].
3. Remove stone [1,2] because it shares the same row as [1,0].
4. Remove stone [1,0] because it shares the same column as [0,0].
5. Remove stone [0,1] because it shares the same row as [0,0].
Stone [0,0] cannot be removed since it does not share a row/column with another stone still on the plane.


"""

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        
        ''' 

        Logic:

        considering every stone as a vertex, and there exists an edge between the vertices, if the stones lie in the same row or same columns. We then find connected components. All Stones in the connceted component, have either common row or column, so we can remove all but one stone from each connected component. So, maximum number of stones that can be removed from each connected components are calculated as follows: 
        total number of vertices/ nodes - stones that cannot be removed ( = 1 each from every connected component = number of connected component)
        thus, equal to total number of nodes - number of connected components

        '''

        # Initialize graph
        ''' 
        nodes: stones
        edges: between nodes if they share same row or column
        stone_graph: adjacency list representing the graph
        '''
        stone_graph = defaultdict(list)

        # Iterate through all pairs of stones
        for i, (x, y) in enumerate(stones):

            # check for edges
            for j in range(i):

                a, b = stones[j]

                # If two stones share the same row or column, add edges to the adjacency list
                if x == a or y == b:
                    stone_graph[i].append(j)
                    stone_graph[j].append(i)
                
        # dfs function to find connected component
        def _dfs(node, visited):
            # once visited, mark true 
            visited[node] = True
            # for every neighbor node, do dfs further
            for neighbor in stone_graph[node]:
                if not visited[neighbor]:
                     _dfs(neighbor, visited)
        
        # count number of components
        num_components = 0
        visited = [False for i in range(len(stones))]

        # For every non-visited node, do dfs to find number of connected components
        for i in range(len(stones)):
            if not visited[i]:
                _dfs(i,visited)
                num_components+=1

        # retun max count of stones that can be removed
        count = len(stones) - num_components
        return count
