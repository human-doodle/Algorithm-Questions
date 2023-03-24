'''
PROBLEM STATEMENT: 
leetcode: https://leetcode.com/problems/dungeon-game/description/

'''

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m = len(dungeon)
        #  n is the number if rooms in a floor
        n = len(dungeon[0])
    
 
        dp = [[math.inf] * (n+1) for _ in range(m+1)]
        
        # We asume the minimum starting energy to be 1
        dp[m][n-1], dp[m-1][n] = 1, 1
        
        for floor in range(m-1, -1, -1):
            
                    for room in range(n-1, -1, -1):
                        
                        neg_energy_required_at_index = min(dp[floor+1][room], dp[floor][room+1]) - dungeon[floor][room]
                        energy_required_at_index = -neg_energy_required_at_index
                        dp[floor][room] = 1 if energy_required_at_index >= 0 else neg_energy_required_at_index
            
        minimum_starting_energy = dp[0][0]
        
        return minimum_starting_energy

