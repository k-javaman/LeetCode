class Solution:
    def isPalindrome(self, s: str) -> bool:
        # extra memory for new string
        newStr = ""

        for c in s:
            if self.alphaNum(c):
                newStr += c.lower()
                # [::-1] --> reverse order
        return newStr == newStr[::-1]
    
    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
               ord('a') <= ord(c) <= ord('z') or
               ord('0') <= ord(c) <= ord('9'))
            
        