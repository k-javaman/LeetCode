class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Create a new string that contains only the alphanumeric characters of the input string in lowercase
        newStr = ""

        for c in s:
            # Check if the character is alphanumeric using the alphaNum() method
            if self.alphaNum(c):
                # Add the lowercase version of the character to newStr
                newStr += c.lower()

        # Check if newStr is equal to its reverse (i.e., if it is a palindrome)
        return newStr == newStr[::-1]

    def alphaNum(self, c):
        # Check if the ASCII value of the input character falls within certain ranges
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))
        