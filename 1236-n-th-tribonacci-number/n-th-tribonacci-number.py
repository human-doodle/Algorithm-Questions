class Solution:
    def tribonacci(self, n: int) -> int:
        return self._tribonacci(n, {})

    def _tribonacci(self, n, memo):
        if n in memo:
            return memo[n]
        if n == 0 :
            return 0
        if n == 2 or n == 1:
            return 1
        memo[n] = self._tribonacci(n-1, memo)+self._tribonacci(n-2, memo)+self._tribonacci(n-3, memo)
        return memo[n]
        