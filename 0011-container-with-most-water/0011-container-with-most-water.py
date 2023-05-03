class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Initialize variables
        l, r = 0, len(height) - 1
        res = 0
        h = max(height)

        # Loop until pointers meet
        while l < r:
            # Compute area of container
            res = max(res, min(height[l], height[r]) * (r - l))

            # Move pointer corresponding to shorter line
            if height[l] < height[r]:
                l += 1
            elif height[r] <= height[l]:
                r -= 1

            # Check if remaining area can be greater than current maximum
            if (r-l) * h <= res:
                break

        # Return maximum area seen so far
        return res