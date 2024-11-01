# Leetcode Problem 22
# Link: https://leetcode.com/problems/generate-parentheses/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # only add open paranthesis if open < n
        # only add close paranthesis if closed < open
        # valid IIF open == close == n
        
        stack = []
        output = []

        def backtrack(open, close):
            if open == close == n:
                output.append("".join(stack))
                return
            
            if open < n:
                stack.append("(")
                backtrack(open + 1, close)
                stack.pop()
            
            if close < open:
                stack.append(")")
                backtrack(open, close + 1)
                stack.pop()
        
        backtrack(0, 0)
        return output