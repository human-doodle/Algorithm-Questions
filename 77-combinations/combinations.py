class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        def _combine(arr, k):
            if k == 0:
                return [[]]
            if k>len(arr):
                return []

            first = arr[0]
            partial = _combine(arr[1:], k-1)
            result = []
            for l in partial:
                result.append([first, *l])

            return result + _combine(arr[1:], k)
        
        return _combine(list(range(1, n + 1)), k)

