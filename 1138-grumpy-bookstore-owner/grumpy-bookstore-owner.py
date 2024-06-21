class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        
        # Calculate the initial total satisfaction without any secret technique
        total_satisfied = sum(customers[i] for i in range(n) if grumpy[i] == 0)
        
        # Calculate the additional satisfaction we can get by using the secret technique in the first 'minutes' period
        additional_satisfied = sum(customers[i] for i in range(minutes) if grumpy[i] == 1)
        
        # Store the maximum additional satisfaction found
        max_additional_satisfied = additional_satisfied
        
        # Sliding window to calculate additional satisfaction for each 'minutes' period
        for i in range(minutes, n):
            if grumpy[i] == 1:
                additional_satisfied += customers[i]
            if grumpy[i - minutes] == 1:
                additional_satisfied -= customers[i - minutes]
            
            max_additional_satisfied = max(max_additional_satisfied, additional_satisfied)
        
        # The result is the initial satisfied customers plus the maximum additional satisfied customers
        return total_satisfied + max_additional_satisfied