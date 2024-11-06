# Leetcode Problem 84
# Link: https://leetcode.com/problems/largest-rectangle-in-histogram/

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # [(idx, ht), (idx, ht), ..]
        maxArea = 0

        for i, curr in enumerate(heights):
            idx = i
            while stack and curr < stack[-1][1]:
                maxArea = max(maxArea, stack[-1][1] * (i - stack[-1][0]))
                idx = stack[-1][0]
                stack.pop()
            
            stack.append((idx, curr))

        i += 1
        while stack:
            maxArea = max(maxArea, stack[-1][1] * (i - stack[-1][0]))
            stack.pop()
        
        return maxArea




