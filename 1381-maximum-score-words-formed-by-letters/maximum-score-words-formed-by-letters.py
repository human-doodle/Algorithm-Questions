class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:

        # Calculate the frequency of each letter in the given letters list
        letter_count = Counter(letters)
        
        # Calculate the score for each word
        word_scores = []
        word_letter_counts = []
        
        for word in words:
            word_count = Counter(word)
            word_score = sum(score[ord(char) - ord('a')] * count for char, count in word_count.items())
            word_scores.append(word_score)
            word_letter_counts.append(word_count)
        
        def can_form(word_count, letter_count):
            for char, count in word_count.items():
                if letter_count[char] < count:
                    return False
            return True
        
        def update_letter_count(letter_count, word_count, increment):
            for char, count in word_count.items():
                letter_count[char] += count * increment
        
        # Backtracking to find the maximum score
        def backtrack(index, current_score):
            if index == len(words):
                return current_score
            
            max_score = current_score
            
            # Option 1: Skip the current word
            max_score = max(max_score, backtrack(index + 1, current_score))
            
            # Option 2: Include the current word (if possible)
            word_count = word_letter_counts[index]
            if can_form(word_count, letter_count):
                update_letter_count(letter_count, word_count, -1)
                max_score = max(max_score, backtrack(index + 1, current_score + word_scores[index]))
                update_letter_count(letter_count, word_count, 1)
            
            return max_score
        
        return backtrack(0, 0)
