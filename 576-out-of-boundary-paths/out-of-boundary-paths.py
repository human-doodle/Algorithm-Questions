class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        MOD = 10 ** 9 + 7

        @lru_cache(None)
        def count_paths(i, j, moveLeft):
            # Base cases
            if i < 0 or i == m or j < 0 or j == n:
                return 1
            if moveLeft == 0:
                return 0

            # Explore all possible moves
            total_paths = 0
            for a, b in moves:
                new_i, new_j = i + a, j + b
                total_paths = (total_paths + count_paths(new_i, new_j, moveLeft - 1)) % MOD

            return total_paths

        return count_paths(startRow, startColumn, maxMove)