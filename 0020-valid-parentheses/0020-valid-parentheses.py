class Solution:
    def isValid(self, s: str) -> bool:
        # Create an empty stack to store opening brackets
        stack = []

        # Iterate over each character in the string
        for char in s:
            # If the character is an opening bracket, push it onto the stack
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            else:
                # If the stack is empty and we encounter a closing bracket, the brackets are not balanced
                if not stack:
                    return False

                # If the character is a closing bracket, pop the top element from the stack and
                # check if it matches the corresponding opening bracket
                if char == ')' and stack[-1] == '(':
                    stack.pop()
                elif char == '}' and stack[-1] == '{':
                    stack.pop()
                elif char == ']' and stack[-1] == '[':
                    stack.pop()
                else:
                    # If the brackets do not match, they are not balanced
                    return False

        # If there are any remaining opening brackets on the stack, the brackets are not balanced
        return not stack