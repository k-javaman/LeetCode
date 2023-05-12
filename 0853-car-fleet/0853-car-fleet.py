class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p, s] for p, s in zip(position, speed)] #List Comprehension

        stack = [] # How many car fleets we have at the end
        for p, s in sorted(pair)[::-1]: # Reverse Sorted Order
            stack.append((target - p) / s)
            # Does it overlap with the other one on the top of the stack
            # 2 is the condition to make collide
            # to append the value and compare, we use if statement not while
            while len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)

# using position and time to calculate the time to distance value!
# List Comprehension and Reverse Sorted Order
# Start from right(closest to destination) to left not to check two speed conditions