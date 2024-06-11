class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = {}
        for num in arr1:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        # Step 2: Sort arr1 according to the order in arr2
        result = []
        for num in arr2:
            if num in count:
                result.extend([num] * count[num])
                del count[num]
        
        # Step 3: Sort the remaining elements not in arr2
        remaining = sorted([num for num in count.keys() for _ in range(count[num])])
        
        # Combine the two parts
        result.extend(remaining)
        
        return result