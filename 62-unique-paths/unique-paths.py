class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # row = [1] * n

        # for i in range(m-1):
        #     newrow = [1] * n
        #     for j in range(n-2, -1, -1):
        #         newrow[j] = newrow[j+1] + row[j]
        #     row = newrow
        # return row[0]

        # o(n+m) o(n)

        # recursion
        def check(i, j):
            if i<0 or j<0 or i>=m or j>=n:
                return False
            return True
        @cache
        def helper(i,j):
            if not check(i, j):
                return 0
            else:
                if j==n-1 and i==m-1:
                    return 1
                else:
                    # move right and down
                    return helper(i+1,j)+helper(i, j+1)
        return helper(0,0)

        # TLE without cache
        