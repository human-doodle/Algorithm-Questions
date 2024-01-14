class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        freq_word1 = [0] * 26
        freq_word2 = [0] * 26

        # Update frequency array for word1
        for char in word1:
            freq_word1[ord(char) - ord('a')] += 1

        # Update frequency array for word2
        for char in word2:
            freq_word2[ord(char) - ord('a')] += 1

        # Check if both words have the same set of characters
        for i in range(26):
            if (freq_word1[i] == 0 and freq_word2[i] != 0) or (freq_word1[i] != 0 and freq_word2[i] == 0):
                return False

            # Check if frequencies of characters match between word1 and word2
            freq = freq_word1[i]
            found_match = False
            for j in range(26):
                if freq == freq_word2[j]:
                    found_match = True
                    freq_word2[j] = -1  # Mark the frequency as visited
                    break

            if not found_match:
                return False

        return True