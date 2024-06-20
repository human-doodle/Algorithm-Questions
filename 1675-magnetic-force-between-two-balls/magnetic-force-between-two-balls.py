class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        # Sort the positions to facilitate distance calculation
        position.sort()

        # Helper function to check if placing m balls with at least `force` distance is feasible
        def feasible(force: int) -> bool:
            # Start placing the first ball
            x, k = position[0], 1
            for i in range(1, len(position)):
                if position[i] - x >= force:
                    x = position[i]
                    k += 1
                    if k == m:
                        return True
            return False

        # Initialize binary search range
        l, r = 1, (position[-1] - position[0]) // (m - 1)

        # Perform binary search
        while l < r:
            mid = l + (r - l + 1) // 2
            if feasible(mid):
                l = mid
            else:
                r = mid - 1

        # Return the maximum minimum distance found
        return l
