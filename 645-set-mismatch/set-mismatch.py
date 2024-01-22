class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        l = len(nums)
        seen = set()
        expected_sum = l*(l+1)//2
        num_sum = 0
        for n in nums:
            if n in seen:
                duplicate = n
            seen.add(n)
            num_sum+=n
        return [duplicate, (residue:=(expected_sum-num_sum)+duplicate)]     
   
        