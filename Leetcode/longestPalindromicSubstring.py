# Leetcode Problem 5
# Link: https://leetcode.com/problems/longest-palindromic-substring/

# O(N^2)
# Logic
# For each character in the string, treat it as the center and expand outward while the characters on both sides match.
# Repeat this for each pair of adjacent characters (to handle even-length palindromes).
# Track the longest palindrome found during these expansions.

class Solution:
    def longestPalindrome(self, s: str) -> str:
        output = ""
        length = 0

        for i in range(len(s)):
            # odd length
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > length:
                    output = s[l:r+1]
                    length = r - l + 1
                l -= 1
                r += 1
            
            # even length
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > length:
                    output = s[l:r+1]
                    length = r - l + 1
                l -= 1
                r += 1

        return output


# O(N^3)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        output = ""
        left, right = 0, 0

        while left <= right and right < len(s):
            substring = s[left:right+1]
            if substring == substring[::-1] and len(substring) > len(output):
                output = substring
            right += 1
            if right == len(s):
                left += 1
                right = left
        
        return output