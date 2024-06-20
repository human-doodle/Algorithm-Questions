class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        def _longestPalindromeSubseq(s, start, end, memo):
            key = (start, end)
            if key  in memo:
                return memo[(start, end)]
            if start > end:
                return 0
            if start == end:
                return 1
            if s[start] == s[end]:
                memo[key] = 2 + _longestPalindromeSubseq(s, start+1, end-1, memo)
                return memo[key]
            else:
                memo[key] = max(
                    _longestPalindromeSubseq(s, start+1, end, memo), 
                    _longestPalindromeSubseq(s, start, end-1, memo)
                    )
                return memo[key]

        return _longestPalindromeSubseq(s, 0, len(s)-1, {})
        