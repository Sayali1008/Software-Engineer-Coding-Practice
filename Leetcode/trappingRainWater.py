# Leetcode Problem 42
# Link: https://leetcode.com/problems/trapping-rain-water/

# MEMORY = O(N)
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        maxLeft, maxRight = [0] * n, [0] * n
        minLR = [0] * n

        for i in range(1, n):
            maxLeft[i] = max(maxLeft[i-1], height[i-1])
        
        for i in range(n-2, -1, -1):
            maxRight[i] = max(maxRight[i+1], height[i+1])
        
        for i in range(n):
            minLR[i] = min(maxLeft[i], maxRight[i])
        
        output = 0
        for i in range(n):
            output += max(minLR[i] - height[i], 0)
        
        return output

# MEMORY: O(1)
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        output = 0
        l, r = 0, len(height) - 1
        maxLeft, maxRight = height[l], height[r]

        while l < r:
            if maxLeft < maxRight:
                l += 1
                maxLeft = max(maxLeft, height[l])
                output += max(maxLeft - height[l], 0)
            else:
                r -= 1
                maxRight = max(maxRight, height[r])
                output += max(maxRight - height[r], 0)
        
        return output
