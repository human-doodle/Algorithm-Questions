class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        min_freq = [float('inf')]*26 # for all alphabets

        for word in words:
            char_count = [0]*26
            for char in word:
                char_count[ord(char)-ord('a')]+=1
            for i in range(26):
                min_freq[i] = min(char_count[i], min_freq[i])

        result = []
        for i in range(26): 
            for j in range(min_freq[i]):
                result.append(chr(i+ord('a')))
        return result
            