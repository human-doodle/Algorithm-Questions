class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # dp = [[0]*(len(text1)+1) for i in range(len(text2)+1)]
        # for i in range(len(text2)-1, -1, -1):
        #     for j in range(len(text1)-1, -1, -1):
        #         if text2[i] == text1[j]:
        #             dp[i][j]=1 + dp[i+1][j+1]
        #         else:
        #             dp[i][j] = max(dp[i][j+1], dp[i+1][j])
        # return dp[0][0]

        def _longestCommonSubsequence(text1, text2, s1, s2, memo):
            key = (s1, s2)
            if key in memo:
                return memo[key]
            if s1 >=len(text1) or s2>=len(text2):
                return 0
            if text1[s1] == text2[s2]:
                memo[key] =  1 + _longestCommonSubsequence(text1, text2, s1+1, s2+1, memo)
                return memo[key]
            else:
                memo[key] = max(
                    _longestCommonSubsequence(text1, text2, s1+1, s2, memo),
                    _longestCommonSubsequence(text1, text2, s1, s2+1, memo))
                return memo[key]
                
        return _longestCommonSubsequence(text1, text2, 0, 0, {})