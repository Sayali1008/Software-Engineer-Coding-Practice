# Leetcode Problem 567
# Link: https://leetcode.com/problems/permutation-in-string/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        output = 0
        left, right = 0, 0
        len1 = len(s1)
        count1 = dict()
        for ch in s1:
            count1[ch] = 1 + count1.get(ch, 0)
        
        count2 = dict()
        while right < len(s2):
            count2[s2[right]] = 1 + count2.get(s2[right], 0)
            if (right - left + 1) == len1:
                if count1 == count2:
                    return True
                count2[s2[left]] -= 1
                if count2[s2[left]] == 0:
                    count2.pop(s2[left])
                left += 1
            right += 1

        return False