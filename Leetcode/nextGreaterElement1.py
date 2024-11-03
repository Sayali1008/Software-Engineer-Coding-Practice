# Leetcode Problem 496
# Link: https://leetcode.com/problems/next-greater-element-i/

# TIME: O(N+M)
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_dict = { val:i for (i, val) in enumerate(nums1) }
        output = [-1] * len(nums1)
        stack = [] # always decreasing

        for num in nums2:
            while stack and num > stack[-1]:
                output[nums1_dict[stack[-1]]] = num
                stack.pop()

            if num in nums1_dict:
                stack.append(num)

        return output

# TIME: O(N*M)
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums2Dict = {}
        for i in range(len(nums2)):
            nums2Dict[nums2[i]] = i
        
        output = [-1] * len(nums1)
        for i in range(len(nums1)):
            j = nums2Dict[nums1[i]] + 1
            while j < len(nums2):
                if nums2[j] > nums1[i]:
                    output[i] = nums2[j]
                    break
                j += 1

        return output
