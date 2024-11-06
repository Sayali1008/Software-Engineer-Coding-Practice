# Leetcode Problem 424
# Link: https://leetcode.com/problems/longest-repeating-character-replacement/

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, right = 0, 0
        output = 0
        charCount = dict()

        while right < len(s):
            charCount[s[right]] = 1 + charCount.get(s[right], 0)
            while (right - left + 1) - max(charCount.values()) > k:
                charCount[s[left]] -= 1
                left += 1
            output = max(output, (right - left + 1))
            right += 1
    
        return output



