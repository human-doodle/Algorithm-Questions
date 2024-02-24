class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        adj = [[] for _ in range(n)]

        # Build adjacent lists
        for meet in meetings:
            x, y, time = meet
            adj[x].append((time, y))
            adj[y].append((time, x))

        known = [float('inf')] * n
        secret_holders = []
        pq = [(0, 0), (0, firstPerson)]  # min heap

        while pq:
            s, x = heappop(pq)
            
            if known[x] != float('inf'):
                continue

            # print(f"knowing secret time={s}, person={x}")
            secret_holders.append(x)
            known[x] = s

            for t, y in adj[x]:
                if known[y] != float('inf') or t < s:
                    continue  # known or too early met

                heappush(pq, (t, y))

        return secret_holders