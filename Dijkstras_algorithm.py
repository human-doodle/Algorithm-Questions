import heapq

def dijkstra(graph, start):
    '''

    graph: nodes and edges with weights/ cost on each edge:
      dictionary where the keys are the nodes and the values 
      are dictionaries containing the neighbors and their corresponding edge weights

    start: start is the node from which to start the search

    '''
    # Initialize distances and visited nodes

    # since finding the minimum distance, we initialize with infinity
    distances = {node: float('inf') for node in graph}
    # distance of starting node is 0
    distances[start] = 0
    # visited nodes are maintained as set
    visited = set()

    # Initialize heap with start node
    heap = [(0, start)]

    while heap:
        # Pop the node with the smallest tentative distance
        (dist, node) = heapq.heappop(heap)

        # Ignore nodes that have already been visited
        if node in visited:
            continue

        # Mark the node as visited
        visited.add(node)

        # Update distances to neighbors by dfs
        for neighbor, weight in graph[node].items():
            if neighbor not in visited:
                # add the weight of the current edge to existing distance
                new_distance = distances[node] + weight

                # if the new distance is less than the previous distance/ weight assigned, update
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    # push the updated vertex and the minimum disance see so far to the heap 
                    heapq.heappush(heap, (new_distance, neighbor))

    return distances

  
#  test

graph = {
    'A': {'B': 1},
    'B': {'A': 1, 'C': 9},
    'C': { 'B': 2},
    'D':{}
}
start= 'A'

dijkstra(graph, start)
