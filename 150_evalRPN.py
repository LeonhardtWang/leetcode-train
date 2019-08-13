class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        :type tokens: List[str]
        :rtype: int
        """
        oper_set = {'+', '-', '*', '/'}
        stack = []
        for t in tokens:
            if t not in oper_set:
                stack.append(t)
            else:
                b, a = stack.pop(), stack.pop()
                stack.append(str(int(eval(a+t+b))))
        return stack[-1]
        
print(Solution().evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))