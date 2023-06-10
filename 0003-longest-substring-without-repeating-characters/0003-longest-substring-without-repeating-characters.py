class Solution:
    # Function to find the length of the longest substring without repeating characters
    def lengthOfLongestSubstring(self, s: str) -> int:

        # Create an empty set to store the unique characters in the current window
        charSet = set()

        # Initialize a left pointer at the start of the string
        l = 0

        # Initialize the result to store the length of the longest substring
        res = 0

        # Start the right pointer to iterate over the string
        for r in range(len(s)):

            # While loop to check if the character at the right pointer's position is already in the set
            while s[r] in charSet:

                # If we found a repeating character, we remove the character at the left pointer's position from the set
                charSet.remove(s[l])

                # Move the left pointer to the right
                l += 1

                # After moving left pointer, add the character at the right pointer's position to the set
            charSet.add(s[r])

            # Update the result with the maximum length between the previous result and the current length of substring
            res = max(res, r - l + 1)

            # Return the length of the longest substring without repeating characters
        return res