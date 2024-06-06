class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize!=0:
            return False

        cards = {}
        for card in hand:
            cards[card] = cards.get(card, 0)+1

        sorted_cards = sorted(cards.keys())

        for card in sorted_cards:

            count = cards[card]
            if count==0:
                continue
             
            for i in range(groupSize):
                if card+i not in cards:
                    return False
                if cards[card+i] < count:
                    return False
                cards[card+i]-=count
                
        return True

