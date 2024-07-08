class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #Time Complexity: O(n)
        #Space Complexity: O(n)
        stack = []
        def op(a,b, opr):
            if opr == '+':
                return int(a + b)
            if opr == '-':
                return int(a - b)
            if opr == '*':
                return int(a * b)
            if opr == '/':
                return int(a / b)
        
        
        operation = set('+-*/')
        for token in tokens:
            if token in operation:
                b = stack.pop()
                a = stack.pop()
                stack.append(op(a,b,token))     
            else:
                stack.append(int(token))
        
        return stack.pop()
