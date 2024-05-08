class Solution(object):
    
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = set()

        # sort first and two pointers
        nums.sort()
        for i in range(len(nums)):
            if i!=0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1,len(nums)-1
            while l<r:
                sum = nums[l]+nums[r] + nums[i] 
                if sum == 0 and i!=l:
                    res.add(tuple(sorted([nums[i], nums[l], nums[r]])))
                    l += 1
                    r -= 1
                    # skip the duplicates:
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif sum < 0:
                    l+=1
                else:
                    r-=1
        return res




        # fix one element and 2some poblem O(n^2logn)
        # for i in range(len(nums)):
        #     s = {}
        #     for j in range(i+1, len(nums)):
        #         third = -(nums[i]+nums[j])
        #         if third in s:
        #             temp = [nums[i], nums[j], third]
        #             temp.sort()
        #             res.add(tuple(temp))
        #             continue
        #         s[nums[j]] = j
                
        # return res

        # tle O(n^3logn: sorting and for loop) O(1)
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         for k in range(j+1, len(nums)):
        #             if nums[i]+nums[j]+nums[k] == 0:
        #                 if tuple(sorted([nums[i], nums[j], nums[k]])) not in res:
        #                     res.add(tuple(sorted([nums[i], nums[j], nums[k]])))
        # return res
