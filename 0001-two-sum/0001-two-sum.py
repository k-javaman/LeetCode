class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} # Create an empty dictionary to store previously seen values and their indices

        for i, n in enumerate(nums): # Loop through the list 'nums' using 'enumerate' to get index 'i' and value 'n'
            diff = target - n # Calculate the difference between 'target' and 'n'
            if diff in prevMap: # Check if 'diff' is present in 'prevMap'
                return [prevMap[diff], i] # If 'diff' is present in 'prevMap', return a list of indices [prevMap[diff], i]
            prevMap[n] = i # Add the current value 'n' and its index 'i' to 'prevMap' for future reference
        return # If no pair of numbers is found that adds up to 'target', return None
    
    #Not solved yet