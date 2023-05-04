class Solution:
    def isValid(self, s: str) -> bool:
        # Create an empty stack to store opening brackets
        stack = []

        # Create a dictionary to map closing brackets to their corresponding opening brackets
        closeToOpen = { ")" : "(", "]" : "[", "}": "{"}

        # Iterate over each character in the string
        for c in s:
            # If the character is a closing bracket, check if it matches the top element of the stack
            # if stack -> if stack is not empty,
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    # If the brackets do not match, they are not balanced
                    return False
            else:
                # If the character is an opening bracket, push it onto the stack
                stack.append(c)

        # If there are any remaining opening brackets on the stack, the brackets are not balanced
        return True if not stack else False