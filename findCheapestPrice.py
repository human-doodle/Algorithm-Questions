"""

link: https://leetcode.com/problems/cheapest-flights-within-k-stops/description/

787. Cheapest Flights Within K Stops

There are n cities connected by some number of flights. You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.

You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.

 

Example 1:


Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1
Output: 700
Explanation:
The graph is shown above.
The optimal path with at most 1 stop from city 0 to 3 is marked in red and has cost 100 + 600 = 700.
Note that the path through cities [0,1,2,3] is cheaper but is invalid because it uses 2 stops.


"""

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

