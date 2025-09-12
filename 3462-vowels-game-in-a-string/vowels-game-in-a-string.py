class Solution:
    def doesAliceWin(self, s: str) -> bool:
        # Define the set of vowels for efficient lookup
        vowels = {'a', 'e', 'i', 'o', 'u'}
      
        # Check if any character in the string is a vowel
        # Returns True if at least one vowel exists, False otherwise
        return any(char in vowels for char in s)