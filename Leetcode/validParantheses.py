# Leetcode Problem 20
# Link: https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        open_to_close = { '(':')', '[':']', '{':'}' }
        close_to_open = { ')':'(', ']':'[', '}':'{' }
        stack = []

        if not s or s[0] in close_to_open:
            return False

        for ch in s:
            if ch in open_to_close.keys():
                stack.append(ch)
            elif ch in close_to_open.keys():
                if stack and stack[-1] == close_to_open[ch]:
                    stack.pop()
                else:
                    return False

        if not stack:
            return True
        return False
