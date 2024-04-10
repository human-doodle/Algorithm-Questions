class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        # Sort the deck
        deck.sort()
        
        # Initialize an empty result array
        result = [0] * len(deck)
        
        # Initialize a queue to keep track of the indices in the result array
        queue = collections.deque(range(len(deck)))
        
        # Iterate through the sorted deck
        for card in deck:
            # Place the current card at the first available index in the result array
            result[queue.popleft()] = card
            
            # If there are still cards in the deck, move the next top card to the bottom
            if queue:
                queue.append(queue.popleft())
        
        return result