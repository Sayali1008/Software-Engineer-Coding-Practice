# Leetcode Problem 74
# Link: https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        low, high = 0, (m * n) - 1

        while low <= high:
            mid = (low + high) // 2
            if matrix[mid//n][mid%n] == target:
                return True
            
            if matrix[mid//n][mid%n] < target:
                low = mid + 1
            else:
                high = mid - 1

        return False