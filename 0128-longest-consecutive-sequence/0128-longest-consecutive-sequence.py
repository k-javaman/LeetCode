class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # create a set of unique numbers
        numSet = set(nums)
        # initialize the longest sequence length to zero
        longest = 0

        # iterate over each number in the input list
        for n in nums:
            # check if it's the start of a sequence
            if(n - 1) not in numSet:
                # initialize the length of the current sequence to zero
                length = 0
                # iterate over each number in the current sequence
                while (n + length) in numSet:
                    # increment the length of the current sequence
                    length += 1
                # update the longest sequence length if necessary
                longest = max(length, longest)
        # return the length of the longest consecutive subsequence
        return longest

# The purpose of this code is to find the length of the longest consecutive subsequence in an input list of integers.
# 
# The code first creates a set of unique numbers from the input list using Python’s built-in set() function. 
# This is done to remove any duplicates from the input list.
# 
# It then initializes a variable called longest to zero. 
# This variable will be used to keep track of the length of the longest consecutive subsequence found so far.
# 
# The code then iterates over each number in the input list using a for loop. 
# For each number, it checks if it’s the start of a sequence by checking if n - 1 is not in numSet. 
# If it is not, then it means that n is the start of a new sequence.
# 
# The code then initializes a variable called length to zero. 
# This variable will be used to keep track of the length of the current consecutive subsequence.
# 
# It then enters a while loop that iterates over each number in the current consecutive subsequence. 
# It does this by checking if n + length is in numSet. 
# If it is, then it increments length by one and continues with the next iteration of the loop. 
# If it isn’t, then it means that we’ve reached the end of the current consecutive subsequence.
# 
# Finally, it updates longest with either length or its current value (whichever is greater) and 
# continues with the next iteration of the for loop.
# 
# Once all numbers have been processed, it returns longest, 
# which represents the length of the longest consecutive subsequence found in the input list.
# 
# 
