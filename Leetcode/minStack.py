# Leetcode Problem 155
# Link: https://leetcode.com/problems/min-stack/

class MinStack:
    def __init__(self):
        self.stack = []
        self.minVal = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minVal:
            self.minVal.append(val)
        elif val <= self.minVal[-1]:
            self.minVal.append(val)
        else:
            self.minVal.append(self.minVal[-1])

    def pop(self) -> None:
        self.stack = self.stack[:-1]
        self.minVal = self.minVal[:-1]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minVal[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()