# Leetcode Problem 704
# Link: https://leetcode.com/problems/binary-search/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = low + int((high - low)/2)

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high -= 1
            else:
                low += 1
                    
        return -1


        