class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        arr.append(0)
        stack = (
            []
        )  # The monotonic stack to track the nearest smaller element to the left for each element in the array.
        result = 0

        for i in range(len(arr)):
            while stack and arr[i] < arr[stack[-1]]:
                # Pop the top element from the stack
                index = stack.pop()
                # Calculate the contribution of the popped element to the sum
                left = stack[-1] if stack else -1
                result = (result + arr[index] * (i - index) * (index - left)) % MOD
            # Push the current index onto the stack
            stack.append(i)

        return result

        # The left boundary is determined by the element at the top of the stack before popping, and the right boundary is the current index.

        # # brute force O(n^2) : tle
        # MOD = 10**9 + 7
        # result = 0

        # # Generate all subarrays
        # for start in range(len(arr)):
        #     for end in range(start, len(arr)):
        #         # Find the minimum in the current subarray
        #         min_val = min(arr[start:end + 1])
        #         # Update the result with the contribution of the minimum value
        #         result = (result + min_val) % MOD
        # return result
