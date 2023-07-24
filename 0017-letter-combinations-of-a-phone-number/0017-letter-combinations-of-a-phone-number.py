class Solution:
    # Function that takes a string of digits and returns a list of all possible letter combinations that the number could represent
    def letterCombinations(self, digits: str) -> List[str]:
        # Initialize an empty list to store the results
        res = []

        # Dictionary mapping each digit to its corresponding letters on a standard phone keypad
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        
        def backtrack(i, curChar):
            if len(curChar) == len(digits):
                res.append(curChar)
                return
            
            for c in digitToChar[digits[i]]:
                backtrack(i+1, curChar+c)
            
        if digits:
            backtrack(0, "")
        
        return res