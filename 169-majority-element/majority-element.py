class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)

        # Optimal solution, optimise the space: moore's voting algorithm, O(2N); O(1)
        element = nums[0]
        count = 1

        for num in nums[1:]:
            if count == 0:
                element = num
                count += 1
                continue
            if num != element:
                count-=1
            else:
                count+=1
        
        # verify; although in this case, it is guaranteed
        count = 0
        for num in nums:
            if num == element:
                count+=1
        if count>n/2:
            return element
        return -1

        # Brute force
        # n = len(nums)
        # d = dict()
        # for num in nums:
        #     d[num] = d.get(num, 0) + 1
        #     if d[num] > n/2:
        #         return num
        
    # O(n) O(n)
                    