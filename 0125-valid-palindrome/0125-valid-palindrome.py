class Solution:
    def isPalindrome(self, s: str) -> bool:
        # extra memory for new string
        newStr = ""

        for c in s:
            if c.isalnum():
                newStr += c.lower()
                # [::-1] --> reverse order
        return newStr == newStr[::-1]
            
        