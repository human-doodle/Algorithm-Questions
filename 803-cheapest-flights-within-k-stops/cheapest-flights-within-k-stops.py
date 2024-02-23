class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        """

        Cities can be thought of as nodes in a graph.
        The connections between each of the cities can be treated as the edges, and finally,
        The cost of going from one city to another would be the weight of the edges in the graph.

        """
        # intiilaize

        # build graph
        graph = defaultdict(list)
        for source, dest, price in flights:
            graph[source].append((dest, price))
        
        visited = set()

        # min heap
        # price, stop, desination
        heap = [(0, 0, src)]


        while heap:
            curr_price, curr_num_stop, curr_dest = heapq.heappop(heap)
            if curr_dest == dst:
                return curr_price
            if (curr_dest,curr_num_stop ) in visited or curr_num_stop > k:
                continue
            visited.add((curr_dest, curr_num_stop))

            for d, p in graph[curr_dest]:
                heappush(heap, (curr_price+p, curr_num_stop+1, d))

          
        return -1