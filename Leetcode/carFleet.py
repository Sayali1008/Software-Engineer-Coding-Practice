# Leetcode Problem 853
# Link: https://leetcode.com/problems/car-fleet/

# TIME: O(N)
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p,s] for (p,s) in zip(position, speed)]
        stack = []

        # reverse sorted order
        for p, s in sorted(pair)[::-1]:
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
            
        return len(stack)

