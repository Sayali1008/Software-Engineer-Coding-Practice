# Leetcode Problem 739
# Link: https://leetcode.com/problems/daily-temperatures/


# TIME: O(N+M)
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)
        stack = [] # always decreasing

        for i, val in enumerate(temperatures):
            while stack and val > temperatures[stack[-1]]:
                output[stack[-1]] = i - stack[-1]
                stack.pop()
            
            stack.append(i)
        
        return output
