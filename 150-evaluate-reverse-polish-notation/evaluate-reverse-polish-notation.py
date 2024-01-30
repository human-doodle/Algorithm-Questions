class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for t in tokens:
            if t not in ["*","-","/","+"]:
                stack.append(t)
            else:
                y = int(stack.pop())
                x = int(stack.pop())
                print(x,y,t)
                op = {"+": (lambda x,y: x+y), 
                "-": (lambda x,y: x-y),
                "*": lambda x,y:x*y,
                "/": lambda x,y: (float(x))/(float(y))}
                result = op[t] (x,y)
                stack.append(result)
        return int(stack[0])