class Solution:
    def numSteps(self, s: str) -> int:
        num = int(s, 2)
        steps = 0
        while num!=1:
            if num%2 == 0:
                num = num//2
            else:
                num = num + 1
            steps+=1
        return steps
                