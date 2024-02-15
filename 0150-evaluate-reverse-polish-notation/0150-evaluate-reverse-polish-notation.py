class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        def perform(op1, op2, op):
            if op == '+':
                return op1 + op2
            elif op == '-':
                return op1 - op2
            elif op == '*':
                return op1 * op2
            elif op == '/':
                return int(op1 / op2)

        stack = []
        operators = {'+', '-', '*', '/'}

        for ch in tokens:
            if ch in operators:
                op2 = stack.pop()
                op1 = stack.pop()
                answer = perform(op1, op2, ch)
                stack.append(answer)
            else:
                stack.append(int(ch))

        return stack[-1]
    
        