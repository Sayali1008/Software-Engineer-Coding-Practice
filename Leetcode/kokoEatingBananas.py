# Leetcode Problem 875
# Link: https://leetcode.com/problems/koko-eating-bananas/

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)

        while low <= high:
            mid = (low + high) // 2
            total = 0
            for i in piles:
                total += ((i + mid - 1) // mid)
            if total <= h:
                high = mid - 1
            else:
                low = mid + 1
        
        return low