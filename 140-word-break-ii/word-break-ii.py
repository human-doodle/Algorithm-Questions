class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # Convert wordDict to a set for faster lookup
        wordSet = set(wordDict)
        
        # Dynamic programming to store whether a substring can be segmented
        dp = [None] * (len(s) + 1)
        dp[0] = [""]
        
        def backtrack(index):
            if dp[index] is not None:
                return dp[index]
            
            sentences = []
            for i in range(index):
                word = s[i:index]
                if word in wordSet:
                    for sentence in backtrack(i):
                        if sentence:
                            sentences.append(sentence + " " + word)
                        else:
                            sentences.append(word)
            dp[index] = sentences
            return sentences
        
        return backtrack(len(s))
            