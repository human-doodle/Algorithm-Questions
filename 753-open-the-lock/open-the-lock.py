class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        if "0000" in deadends:
            return -1
        
        queue = deque([("0000", 0)])  # (state, turns)
        visited = set("0000")
        
        while queue:
            state, turns = queue.popleft()
            
            if state == target:
                return turns
            
            for i in range(4):
                for d in [-1, 1]:
                    new_state = state[:i] + str((int(state[i]) + d) % 10) + state[i+1:]
                    
                    if new_state not in visited and new_state not in deadends:
                        queue.append((new_state, turns + 1))
                        visited.add(new_state)
        
        return -1