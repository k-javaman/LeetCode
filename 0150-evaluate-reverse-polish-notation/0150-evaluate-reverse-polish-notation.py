class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            # Be careful about the subtract order!  pop order b -> a -> operator
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            # Use int casting + '/'
            # -> The division between two integers always truncates toward zero.
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            # integer!
            else:
                stack.append(int(c))
        return stack[0]