'''
3136. Valid Word

A word is considered valid if:

It contains a minimum of 3 characters.
It contains only digits (0-9), and English letters (uppercase and lowercase).
It includes at least one vowel.
It includes at least one consonant.
You are given a string word.

Return true if word is valid, otherwise, return false.

Notes:

'a', 'e', 'i', 'o', 'u', and their uppercases are vowels.
A consonant is an English letter that is not a vowel.
'''


# Key Ideas:
# We can add a check for the length of s at that start with early return. 
# We initialize two boolean variables, vowel and consonant, representing the
# vowel and consonant constraints. We also define the set of vowels. Then, we 
# iterate over each character in s and check:
#   - if the character is not a digit (not c.isdigit()) and not a letter
#       (not c.isalpha()), then we return False early.
#   - if the character is a vowel, then we set the vowel variable to True.
#   - if the character is a letter and is not a vowel, then we set the 
#       consonant variable to True.
#
# If we exit the for loop without returning early, we return True if both
# vowel and consonant are True. 


# Runtime: O(n) because in the worst case, we iterate through the entire 
# string.

# Space: O(1) because we are storing two booleans and a fixed length set in 
# memory. 


class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False

        vowel = False
        consonant = False
        vowels = {'a', 'e', 'i', 'o', 'u'}

        for c in word:
            if not c.isdigit() and not c.isalpha():
                return False
            
            if c.isalpha():
                c = c.lower()
                if c in vowels:
                    vowel = True
                else:
                    consonant = True
        
        return vowel and consonant