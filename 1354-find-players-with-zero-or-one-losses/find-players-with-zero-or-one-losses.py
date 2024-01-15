class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        w = []
        l = []
        players = set()
        winner_counts = Counter()
        lost_count = Counter() # Track both wins and losses efficiently
        for winner, loser in matches:
            winner_counts[winner]+=1
            lost_count[loser]+=1
            players.add(winner)
            players.add(loser)
        for player in players:
            if winner_counts[player]>0 and lost_count[player]==0 :
                w.append(player)
            if lost_count[player]==1 :
                l.append(player)

        return [sorted(w),sorted(l)]
