# Leetcode Problem 150
# Link: https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
    # Avoid Redundant Code by Using a Dictionary for Operations
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': lambda x, y: int(x / y)  # To ensure truncation toward zero
        }
        
        for token in tokens:
            if token in ops:
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(ops[token](op1, op2))
            else:
                stack.append(int(token))
        
        return stack.pop()

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token == '+':
                op2 = stack.pop()
                op1 = stack.pop()
                total = op1 + op2
                stack.append(total)
            elif token == '-':
                op2 = stack.pop()
                op1 = stack.pop()
                total = op1 - op2
                stack.append(total)
            elif token == '*':
                op2 = stack.pop()
                op1 = stack.pop()
                total = op1 * op2
                stack.append(total)
            elif token == '/':
                op2 = stack.pop()
                op1 = stack.pop()
                total = int(op1 / op2)
                stack.append(total)
            else:
                stack.append(int(token))
    
        return stack[-1]