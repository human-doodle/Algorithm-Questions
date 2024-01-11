class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prefix_arr = [0]

        # calculate prefix value
        cur_sum = 0
        for num in nums:
            cur_sum+=num
            self.prefix_arr.append(cur_sum)
        

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_arr[right+1] - self.prefix_arr[left]
        

# TC: O(n)
# SC: O(n)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)