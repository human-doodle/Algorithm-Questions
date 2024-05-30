class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        prefixXOR = [0] * (n + 1)
        
        # Calculate prefix XOR
        for i in range(n):
            prefixXOR[i + 1] = prefixXOR[i] ^ arr[i]
        
        count = 0
        
        # Iterate through all pairs (i, k) with i < k
        for i in range(n):
            for k in range(i + 1, n):
                # Check if XOR from i to k is 0
                if prefixXOR[i] == prefixXOR[k + 1]:
                    # All possible j values between i and k are valid
                    count += (k - i)
        
        return count