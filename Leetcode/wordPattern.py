# Leetcode Problem 290
# Link: https://leetcode.com/problems/word-pattern/

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        listS = s.split(" ")
        char_to_word = dict()
        word_to_char = dict()
        
        if len(listS) != len(pattern):
            return False

        for i in range(len(pattern)):
            if pattern[i] in char_to_word:
                if listS[i] != char_to_word[pattern[i]]:
                    return False
            elif listS[i] in word_to_char:
                return False
            else:
                char_to_word[pattern[i]] = listS[i]
                word_to_char[listS[i]] = pattern[i]
        
        return True