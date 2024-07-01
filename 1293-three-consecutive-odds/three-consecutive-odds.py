class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        N = len(arr)
        # N=4
        # 0, 1, 2, 3
        for i in range(N-2):
            if arr[i] % 2 != 0 and arr[i+1] % 2 != 0 and arr[i+2] % 2 != 0:
                return True
        return False