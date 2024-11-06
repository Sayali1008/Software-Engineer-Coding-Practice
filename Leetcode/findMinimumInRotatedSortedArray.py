# Leetcode Problem 153
# Link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            if nums[mid+1] < nums[mid]:
                return nums[mid+1]
            if nums[mid] < nums[mid-1]:
                return nums[mid]
            if nums[mid] < nums[-1]:
                high = mid - 1
            elif nums[mid] > nums[-1]:
                low = mid + 1
        
        return 0